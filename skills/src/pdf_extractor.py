import pdfplumber


def extract_text_from_pdf(file_path):
    """
    Extract text from all pages of a PDF resume.
    """

    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text.strip()


# Test with your resume PDF
pdf_path = "skills/resumes/resume_1.pdf"

extracted_text = extract_text_from_pdf(pdf_path)

print("===== EXTRACTED RESUME TEXT =====")
print(extracted_text)