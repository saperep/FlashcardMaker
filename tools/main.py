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
d