import io
import zipfile
from pathlib import Path

import fitz
from docx import Document


def extract_pdf_text(pdf_file):
    text = ""

    pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text


def extract_document_text(uploaded_file):
    if uploaded_file is None:
        return ""

    name = (getattr(uploaded_file, "name", "") or "").lower()
    data = uploaded_file.read()

    if name.endswith(".pdf"):
        pdf = fitz.open(stream=data, filetype="pdf")
        return "\n".join(page.get_text() for page in pdf)

    if name.endswith(".docx"):
        doc = Document(io.BytesIO(data))
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n".join(paragraphs)

    return ""
