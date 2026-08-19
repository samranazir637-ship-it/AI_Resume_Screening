import io
from docx import Document

from utils.pdf_reader import extract_document_text


def test_extract_document_text_handles_docx():
    document = Document()
    document.add_paragraph("Python developer with SQL and Docker skills.")
    buffer = io.BytesIO()
    document.save(buffer)
    buffer.seek(0)

    fake_file = io.BytesIO(buffer.getvalue())
    fake_file.name = "resume.docx"

    text = extract_document_text(fake_file)

    assert "Python developer" in text
    assert "Docker" in text
