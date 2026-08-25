from src.pdf_extractor import extract_text_from_pdf


pdf_path = "data/resumes/sample_resume.pdf"

text = extract_text_from_pdf(pdf_path)

print("===== EXTRACTED RESUME TEXT =====")
print(text)