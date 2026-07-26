import os

from app.utils.loaders import (
    load_pdf,
    load_docx,
    load_txt
)

from app.utils.splitters import split_text


def extract_text(file_path: str):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":

        return load_pdf(file_path)

    elif extension == ".docx":

        return load_docx(file_path)

    elif extension == ".txt":

        return load_txt(file_path)

    else:

        raise Exception(
            "Unsupported File"
        )


def process_file(file_path: str):

    text = extract_text(file_path)

    chunks = split_text(text)

    return {

        "characters": len(text),

        "chunks": len(chunks),

        "preview": chunks[0] if chunks else ""

    }