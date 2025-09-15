# tools/make_qa.py
from __future__ import annotations
import argparse, hashlib, json, os, re, pathlib
from datetime import datetime
from typing import List, Dict, Any, Tuple

import fitz
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
from tqdm import tqdm

# ==== Config ====
EMB_MODEL = "BAAI/bge-m3"
CHUNK_WORDS = 400
TOP_K = 1                  # par chunk on reste focalisé
USE_OLLAMA = False          # sinon met à False et configure OpenAI en bas

# ==== LLM helpers ====
def call_llm_generate(system_prompt: str, excerpt: str, pages: Tuple[int,int]) -> List[Dict[str, Any]]:
    if USE_OLLAMA:
        import ollama
        prompt = f"{system_prompt}\n\n### EXTRAI T (pages {pages[0]}-{pages[1]}):\n{excerpt}\n\n### RÉPONDS:"
        resp = ollama.chat(model="llama3.1:8b-instruct", messages=[{"role":"user","content":prompt}])
        txt = resp["message"]["content"]
    else:
        from openai import OpenAI
        client = OpenAI()
        prompt = f"{system_prompt}\n\n### EXTR AIT (pages {pages[0]}-{pages[1]}):\n{excerpt}\n\n### RÉPONDS:"
        txt = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":prompt}],
            temperature=0.2
        ).choices[0].message.content
    # tolère JSON “pas parfait”
    try:
        return json.loads(txt)
    except Exception:
        # tente extraction grossière de structure JSON
        start = txt.find('['); end = txt.rfind(']')
        return json.loads(txt[start:end+1])

def call_llm_critic(critic_prompt: str, q: Dict[str,Any], excerpt: str) -> Dict[str,Any]:
    payload = {"q": q, "excerpt": excerpt}
    if USE_OLLAMA:
        import ollama, json
        prompt = f"{critic_prompt}\n\nExtrait:\n{excerpt}\n\nCarte:\n{json.dumps(q,ensure_ascii=False,indent=2)}\n\nRéponds JSON:"
        resp = ollama.chat(model="llama3.1:8b-instruct", messages=[{"role":"user","content":prompt}])
        txt = resp["message"]["content"]
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
        return json.loads(txt[start:end+1])

# ==== PDF -> pages ====
def extract_pages(pdf_path: pathlib.Path) -> List[Dict[str, Any]]:
    doc = fitz.open(pdf_path)
    out = []
    for i, p in enumerate(doc):
        text = p.get_text("text")
        out.append({"page": i+1, "text": text})
    return out

def chunk_pages(pages: List[Dict[str,Any]], max_words=CHUNK_WORDS):
    chunks = []
    buf, start = [], None
    for pg in pages:
        words = pg["text"].split()
        if start is None: start = pg["page"]
        buf.append(pg["text"])
        if sum(len(b.split()) for b in buf) >= max_words:
            chunks.append({"pages": (start, pg["page"]), "text": "\n".join(buf)})
            buf, start = [], None
    if buf:
        chunks.append({"pages": (start, pages[-1]["page"]), "text": "\n".join(buf)})
    return chunks

# ==== Déduplication par embedding de question ====
class Deduper:
    def __init__(self):
        self.model = SentenceTransformer(EMB_MODEL)
        self.vecs = None
        self.index = None
        self.qids = []

    def _ensure(self):
        if self.index is None:
            self.index = faiss.IndexFlatIP(1024)  # bge-m3 dim=1024
            self.vecs = np.zeros((0,1024), dtype=np.float32)

    def is_duplicate(self, question: str, threshold=0.90) -> bool:
        self._ensure()
        v = self.model.encode([question], normalize_embeddings=True).astype(np.float32)
        if self.vecs.shape[0] == 0:
            self.vecs = np.vstack([self.vecs, v])
            self.index.add(v)
            return False
        D, I = self.index.search(v, 1)
        is_dup = float(D[0][0]) >= threshold
        if not is_dup:
            self.vecs = np.vstack([self.vecs, v])
            self.index.add(v)
        return is_dup

def qid(q: Dict[str,Any]) -> str:
    h = hashlib.sha256(json.dumps(q, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:12]
    return h

# ==== Markdown writer ====
def write_markdown(md_path: pathlib.Path, header: Dict[str,Any], cards: List[Dict[str,Any]]):
    md_path.parent.mkdir(parents=True, exist_ok=True)
    if not md_path.exists():
        head = f"""---
course: "{header['course']}"
generated_at: "{datetime.now().isoformat(timespec='seconds')}"
---

# Flashcards – {header['course']}
"""
        md_path.write_text(head, encoding="utf-8")

    with md_path.open("a", encoding="utf-8") as f:
        for c in cards:
            _qid = qid(c)
            pages = c.get("pages", [])
            src = f"{header['source']}#p={pages[0]}-{pages[-1]}" if pages else header['source']
            f.write(f"\n---\n### [QID:{_qid}] (type: {c['type']}, pages: {pages})\n")
            f.write(f"**Q.** {c['question']}\n\n")
            if c["type"] == "mcq":
                choices = c.get("choices", [])
                for i, ch in enumerate(choices, 1):
                    f.write(f"{chr(64+i)}) {ch}\n")
                f.write(f"\n**Réponse :** {c.get('correct','?')}\n")
            else:
                f.write(f"**Réponse :** {c['answer']}\n")
            if c.get("why"):
                f.write(f"*Pourquoi:* {c['why']}\n")
            f.write(f"*Source:* {src}\n")

# ==== Main ====
def run(pdf_dir: str, out_notes: str, course_name: str):
    system_prompt = pathlib.Path("tools/prompts/system.md").read_text(encoding="utf-8")
    critic_prompt = pathlib.Path("tools/prompts/critic.md").read_text(encoding="utf-8")
    deduper = Deduper()

    for pdf in sorted(pathlib.Path(pdf_dir).glob("*.pdf")):
        pages = extract_pages(pdf)
        chunks = chunk_pages(pages)

        all_cards = []
        for ch in tqdm(chunks, desc=f"Gen {pdf.name}"):
            raw = call_llm_generate(system_prompt, ch["text"], ch["pages"])
            # critic + filtre + dédup
            for q in raw:
                qc = call_llm_critic(critic_prompt, q, ch["text"])
                keep = qc.get("keep", True)
                if not keep and qc.get("fix"):  # si réparable
                    q = json.loads(qc["fix"])
                if keep and not deduper.is_duplicate(q.get("question","")):
                    q["pages"] = list(range(ch["pages"][0], ch["pages"][1]+1))
                    all_cards.append(q)

        write_markdown(
            pathlib.Path(out_notes) / f"{pdf.stem}_flashcards.md",
            header={"course": course_name, "source": f"data/pdf/{pdf.name}"},
            cards=all_cards
        )

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf-dir", default="data/pdf")
    ap.add_argument("--out-notes", default="notes")
    ap.add_argument("--course", required=True)
    args = ap.parse_args()
    run(args.pdf_dir, args.out_notes, args.course)
