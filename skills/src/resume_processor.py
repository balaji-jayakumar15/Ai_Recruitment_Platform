import re


def clean_text(text):
    """
    Clean extracted resume text.
    """

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove unnecessary spaces around punctuation
    text = re.sub(r"\s([,.])", r"\1", text)

    return text.strip()


def extract_email(text):
    """
    Extract email address from resume text.
    """

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    return match.group(0) if match else ""


def extract_phone(text):
    """
    Extract phone number from resume text.
    """

    pattern = r"(?:\+91[\s-]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    return match.group(0) if match else ""


def process_resume(text):
    """
    Process resume text and extract basic candidate details.
    """

    cleaned_text = clean_text(text)

    candidate = {
        "email": extract_email(cleaned_text),
        "phone": extract_phone(cleaned_text),
        "cleaned_text": cleaned_text
    }

    return candidate