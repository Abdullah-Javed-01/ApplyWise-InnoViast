from pypdf import PdfReader

def extract_text_from_pdf(pdf_path) -> str:
    reader = PdfReader(pdf_path)
    combined_text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            combined_text += page_text + "\n"
    return combined_text.strip()