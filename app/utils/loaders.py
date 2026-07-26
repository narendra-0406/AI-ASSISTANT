from pypdf import PdfReader
from docx import Document

def load_pdf(file_path: str):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        text += page.extract_text() + "\n"

    return text



def load_docx(file_path: str):

    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:

        text += paragraph.text + "\n"

    return text

def load_txt(file_path: str):

    with open(
        file_path,
        encoding="utf-8"
    ) as file:

        return file.read()