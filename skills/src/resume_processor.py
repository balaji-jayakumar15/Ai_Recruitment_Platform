def extract_text_from_txt(file_path):
    """
    Read text from a plain-text resume.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().strip()


# Resume text file
file_path = "skills/resumes/resume1.txt"

# Extract text
extracted_text = extract_text_from_txt(file_path)

print("===== RESUME TEXT =====")
print(extracted_text)