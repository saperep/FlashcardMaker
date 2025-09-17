# tools/make_qa.py
from __future__ import annotations
import argparse, hashlib, json, pathlib, io, os, sys
from datetime import datetime
from typing import List, Dict, Any, Tuple

import fitz  # PyMuPDF
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
from tqdm import tqdm
from PIL import Image
import pytesseract

# ============ Config ============
EMB_MODEL = "BAAI/bge-m3"
CHUNK_WORDS = 400
USE_OLLAMA = False
INDEX_PATH = ".qa_index.json"  # global, à la racine du repo

# ============ LLM helpers ============
def call_llm_generate(system_prompt: str, excerpt: str, pages: Tuple[int, int]) -> List[Dict[str, Any]]:
    if USE_OLLAMA:
        import ollama
        prompt = f"{system_prompt}\n\n### EXTRAIT (pages {pages[0]}-{pages[1]}):\n{excerpt}\n\n### RÉPONDS:"
        txt = ollama.chat(model="llama3.1:8b", messages=[{"role":"user","content":prompt}])["message"]["content"]
    else:
        from openai import OpenAI
        client = OpenAI()
        prompt = f"{system_prompt}\n\n### EXTRAIT (pages {pages[0]}-{pages[1]}):\n{excerpt}\n\n### RÉPONDS:"
        txt = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":prompt}],
            temperature=0.2
        ).choices[0].message.content
    try:
        return json.loads(txt)
    except Exception:
        start = txt.find('['); end = txt.rfind(']')
        if start == -1 or end == -1:
            print("[WARN] LLM did not return a JSON list. Skipping chunk.", file=sys.stderr)
            return []
        return json.loads(txt[start:end+1])

def call_llm_critic(critic_prompt: str, q: Dict[str,Any], excerpt: str) -> Dict[str,Any]:
    if USE_OLLAMA:
        import ollama
        prompt = f"{critic_prompt}\n\nExtrait:\n{excerpt}\n\nCarte:\n{json.dumps(q,ensure_ascii=False,indent=2)}\n\nRéponds JSON:"
        txt = ollama.chat(model="llama3.1:8b", messages=[{"role":"user","content":prompt}])["message"]["content"]
    else:
        from openai import OpenAI
        client = OpenAI()
        prompt = f"{critic_prompt}\n\nExtrait:\n{excerpt}\n\nCarte:\n{json.dumps(q,ensure_ascii=False,indent=2)}\n\nRéponds JSON:"
        txt = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":prompt}],
            temperature=0.0
        ).choices[0].message.content
    try:
        return json.loads(txt)
    except Exception:
        start = txt.find('{'); end = txt.rfind('}')
        if start == -1 or end == -1:
            return {"keep": True}
        return json.loads(txt[start:end+1])

# ============ OCR ============
def page_text_with_ocr(p, dpi=220, lang="eng+fra", min_chars=30) -> str:
    text = (p.get_text("text") or "").strip()
    if len(text) >= min_chars:
        return text
    pix = p.get_pixmap(dpi=dpi, alpha=False)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    ocr = pytesseract.image_to_string(img, lang=lang)
    return (text + "\n" + (ocr or "")).strip()

# ============ PDF / chunk ============
def extract_pages(pdf_path: pathlib.Path) -> List[Dict[str, Any]]:
    doc = fitz.open(pdf_path)
    out = []
    for i, p in enumerate(doc):
        txt = page_text_with_ocr(p)
        out.append({"page": i + 1, "text": txt})
    return out

def chunk_pages(pages: List[Dict[str, Any]], max_words=CHUNK_WORDS):
    chunks = []
    buf, start = [], None
    for pg in pages:
        if start is None:
            start = pg["page"]
        buf.append(pg["text"])
        words_total = sum(len(b.split()) for b in buf)
        if words_total >= max_words:
            end_page = pg["page"]
            chunks.append({"pages": (start, end_page), "text": "\n".join(buf)})
            buf, start = [], None
    if buf:
        chunks.append({"pages": (start, pages[-1]["page"]), "text": "\n".join(buf)})
    return chunks

# ============ Dédup ============
class Deduper:
    def __init__(self):
        self.model = SentenceTransformer(EMB_MODEL)
        self.vecs = None
        self.index = None
    def _ensure(self):
        if self.index is None:
            self.index = faiss.IndexFlatIP(1024)  # bge-m3
            self.vecs = np.zeros((0,1024), dtype=np.float32)
    def is_duplicate(self, question: str, threshold=0.90) -> bool:
        self._ensure()
        v = self.model.encode([question], normalize_embeddings=True).astype(np.float32)
        if self.vecs.shape[0] == 0:
            self.vecs = np.vstack([self.vecs, v]); self.index.add(v); return False
        D, _ = self.index.search(v, 1)
        is_dup = float(D[0][0]) >= threshold
        if not is_dup:
            self.vecs = np.vstack([self.vecs, v]); self.index.add(v)
        return is_dup

class _DeduperSingleton(Deduper): pass
DeduperSingleton = _DeduperSingleton()

# ============ Utils ============
def qid(q: Dict[str,Any]) -> str:
    h = hashlib.sha256(json.dumps(q, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:12]
    return h

def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def load_index(path=INDEX_PATH) -> Dict[str, Any]:
    p = pathlib.Path(path)
    if p.exists():
        try: return json.loads(p.read_text(encoding="utf-8"))
        except Exception: return {}
    return {}
def save_index(idx: Dict[str,Any], path=INDEX_PATH):
    pathlib.Path(path).write_text(json.dumps(idx, indent=2, ensure_ascii=False), encoding="utf-8")

# ============ Markdown (choix visibles pour MCQ) ============
def write_markdown(md_path: pathlib.Path, header: Dict[str,Any], cards: List[Dict[str,Any]]):
    md_path.parent.mkdir(parents=True, exist_ok=True)
    if not md_path.exists():
        head = f"""---
course: "{header['course']}"
generated_at: "{datetime.now().isoformat(timespec='seconds')}"
---

# Flashcards – {header['course']}

> Astuce : cliquez pour dérouler la réponse.
"""
        md_path.write_text(head, encoding="utf-8")

    def page_range(pages: list[int]) -> str:
        if not pages: return ""
        lo, hi = min(pages), max(pages)
        return f"p. {lo}" if lo == hi else f"p. {lo}–{hi}"

    with md_path.open("a", encoding="utf-8") as f:
        for c in cards:
            q = c.get("question", "").strip()
            why = c.get("why", "")
            pages = c.get("pages", [])
            src = f"{header['source']}#p={pages[0]}-{pages[-1]}" if pages else header['source']
            _qid = qid(c)
            f.write(f"\n<!-- QID:{_qid} -->\n")

            label = page_range(pages)
            label_sup = f"  <sup>{label}</sup>" if label else ""
            f.write(f"### {q}{label_sup}\n\n")

            # MCQ: afficher les choix AVANT la réponse repliée
            if c.get("type") == "mcq":
                choices = c.get("choices", [])
                if choices:
                    f.write("**Choix :**\n\n")
                    for i, ch in enumerate(choices, 1):
                        f.write(f"- {chr(64+i)}) {ch}\n")
                    f.write("\n")

            f.write("<details>\n<summary>Afficher la réponse</summary>\n\n")
            if c.get("type") == "mcq":
                f.write(f"**Réponse :** {c.get('correct','?')}\n\n")
            else:
                f.write(f"**Réponse :** {c.get('answer','')}\n\n")
            if why:
                f.write(f"**Pourquoi :** {why}\n\n")
            f.write(f"**Source :** `{src}`\n\n")
            f.write("</details>\n")

# ============ Main ============
def run(pdf_dir: str, out_notes: str, course_name: str, force: bool = False):
    print(f"[INFO] Backend: {'Ollama' if USE_OLLAMA else 'OpenAI'}")
    print(f"[INFO] CWD: {pathlib.Path.cwd()}")
    print(f"[INFO] PDF dir: {pdf_dir}  out: {out_notes}  course: {course_name}  force={force}")

    system_prompt = pathlib.Path("tools/prompts/system.md").read_text(encoding="utf-8")
    critic_prompt = pathlib.Path("tools/prompts/critic.md").read_text(encoding="utf-8")

    pdf_root = pathlib.Path(pdf_dir)
    pdfs = [p for p in pdf_root.rglob("*") if p.is_file() and p.suffix.lower() == ".pdf"]
    pdfs.sort(key=lambda p: p.name.lower())
    print(f"[INFO] Found {len(pdfs)} PDFs: {[p.name for p in pdfs]}")
    if not pdfs:
        print("[ERROR] 0 PDF trouvés. Vérifie le chemin et LFS.", file=sys.stderr)

    index = load_index(INDEX_PATH)
    api_calls = 0

    for pdf in pdfs:
        file_hash = sha256_file(pdf)
        rec = index.get(str(pdf))
        if (not force) and rec and rec.get("hash") == file_hash:
            print(f"[SKIP] {pdf} (unchanged)")
            continue

        print(f"[INFO] Processing {pdf.name}")
        pages = extract_pages(pdf)
        chars_total = sum(len(pg["text"]) for pg in pages)
        print(f"[INFO] {pdf.name}: pages={len(pages)}, chars_total={chars_total}")

        chunks = chunk_pages(pages)
        print(f"[INFO] {pdf.name}: chunks={len(chunks)}")

        all_cards = []
        for ch in tqdm(chunks, desc=f"Gen {pdf.name}"):
            if len(ch["text"].strip()) < 50:
                continue
            api_calls += 1
            print(f"[INFO] Calling LLM for {pdf.name} pages {ch['pages']} (chars={len(ch['text'])})")
            raw = call_llm_generate(system_prompt, ch["text"], ch["pages"])
            for q in (raw or []):
                qc = call_llm_critic(critic_prompt, q, ch["text"])
                keep = qc.get("keep", True)
                if not keep and qc.get("fix"):
                    try:
                        q = json.loads(qc["fix"])
                    except Exception:
                        keep = False
                if keep and not DeduperSingleton.is_duplicate(q.get("question","")):
                    q["pages"] = list(range(ch["pages"][0], ch["pages"][1]+1))
                    all_cards.append(q)

        print(f"[INFO] {pdf.name}: generated {len(all_cards)} cards")
        out_md = pathlib.Path(out_notes) / f"{pdf.stem}_flashcards.md"
        write_markdown(out_md, header={"course": course_name, "source": f"{pdf}"} , cards=all_cards)

        index[str(pdf)] = {
            "hash": file_hash,
            "last_run": datetime.now().isoformat(timespec="seconds"),
            "pages": len(pages),
            "chunks": len(chunks),
            "cards": len(all_cards),
            "out": str(out_md),
        }
        save_index(index, INDEX_PATH)

    print(f"[INFO] Total LLM calls: {api_calls}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf-dir", help="Dossier des PDFs", required=True)
    ap.add_argument("--out-notes", help="Dossier de sortie Markdown", required=True)
    ap.add_argument("--course", required=True)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    run(args.pdf_dir, args.out_notes, args.course, force=args.force)
