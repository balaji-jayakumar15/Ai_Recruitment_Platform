import os
import io
import json


def extract_text_from_pdf(file_path):

    result = {
        "file_name": os.path.basename(file_path) if file_path else "",
        "file_type": "pdf",
        "extraction_status": "failed",
        "full_text": "",
        "pages": [],
        "error": None
    }

    # ---------------------------------------------------------
    # STEP 1 - Validate file path
    # ---------------------------------------------------------

    if not file_path:
        result["error"] = "PDF file path was not provided."
        return result

    if not os.path.exists(file_path):
        result["error"] = "PDF file not found."
        return result

    if not os.path.isfile(file_path):
        result["error"] = "The given path is not a file."
        return result

    if not file_path.lower().endswith(".pdf"):
        result["error"] = "The selected file is not a PDF."
        return result

    # ---------------------------------------------------------
    # STEP 2 - Import PyMuPDF safely
    # ---------------------------------------------------------

    try:
        import fitz
    except ImportError:
        result["error"] = (
            "PyMuPDF is not installed. "
            "Install it using: pip install PyMuPDF"
        )
        return result

    # ---------------------------------------------------------
    # STEP 3 - Open PDF
    # ---------------------------------------------------------

    try:
        document = fitz.open(file_path)
    except Exception as e:
        result["error"] = f"Unable to open PDF: {str(e)}"
        return result

    extracted_pages = []

    # ---------------------------------------------------------
    # STEP 4 - Process every page
    # ---------------------------------------------------------

    try:

        for page_number, page in enumerate(document, start=1):

            page_result = {
                "page": page_number,
                "text": "",
                "method": "none"
            }

            # -------------------------------------------------
            # Try normal PDF text extraction
            # -------------------------------------------------

            try:
                text = page.get_text("text").strip()
            except Exception:
                text = ""

            if text:

                page_result["text"] = text
                page_result["method"] = "text"

            else:

                # ---------------------------------------------
                # OCR fallback
                # ---------------------------------------------

                try:
                    import pytesseract
                    from PIL import Image

                    # Convert PDF page to image
                    pixmap = page.get_pixmap(
                        matrix=fitz.Matrix(2, 2),
                        alpha=False
                    )

                    image_bytes = pixmap.tobytes("png")

                    image = Image.open(
                        io.BytesIO(image_bytes)
                    )

                    # OCR
                    ocr_text = pytesseract.image_to_string(
                        image
                    ).strip()

                    if ocr_text:

                        page_result["text"] = ocr_text
                        page_result["method"] = "ocr"

                    else:

                        page_result["text"] = ""
                        page_result["method"] = "no_text_found"

                except ImportError:

                    page_result["text"] = ""
                    page_result["method"] = "ocr_unavailable"

                except Exception as ocr_error:

                    page_result["text"] = ""
                    page_result["method"] = "ocr_failed"

            extracted_pages.append(page_result)

        document.close()

    except Exception as e:

        try:
            document.close()
        except Exception:
            pass

        result["error"] = f"Error while processing PDF: {str(e)}"
        return result

    # ---------------------------------------------------------
    # STEP 5 - Combine all extracted text
    # ---------------------------------------------------------

    full_text = "\n\n".join(
        page["text"]
        for page in extracted_pages
        if page["text"]
    )

    result["pages"] = extracted_pages
    result["full_text"] = full_text

    # ---------------------------------------------------------
    # STEP 6 - Final status
    # ---------------------------------------------------------

    if full_text.strip():
        result["extraction_status"] = "success"
    else:
        result["extraction_status"] = "no_text_found"

        # Check whether OCR was unavailable
        methods = [
            page["method"]
            for page in extracted_pages
        ]

        if "ocr_unavailable" in methods:
            result["error"] = (
                "No selectable text found. "
                "OCR could not be used because "
                "pytesseract or PIL is unavailable."
            )

    return result


# =============================================================
# MAIN PROGRAM
# =============================================================

if __name__ == "__main__":

    # ---------------------------------------------------------
    # CHANGE ONLY THIS PATH
    # ---------------------------------------------------------

    pdf_path = r"C:\Users\acer\OneDrive\Desktop\ai-recruitment platform\resume.pdf"

    # ---------------------------------------------------------
    # Extract PDF
    # ---------------------------------------------------------

    output = extract_text_from_pdf(pdf_path)

    # ---------------------------------------------------------
    # Print JSON output
    # ---------------------------------------------------------

    print(
        json.dumps(
            output,
            indent=4,
            ensure_ascii=False
        )
    )