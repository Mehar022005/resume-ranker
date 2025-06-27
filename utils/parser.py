import fitz  # PyMuPDF

def parse_resume(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def parse_job_description(file):
    return file.read().decode("utf-8")
