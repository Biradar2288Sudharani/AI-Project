import fitz
import pytesseract

from PIL import Image
from io import BytesIO


class PDFReader:

    @staticmethod
    def extract_text(pdf_path):

        try:

            pytesseract.pytesseract.tesseract_cmd = (
                r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            )

            pdf = fitz.open(pdf_path)

            full_text = ""

            print(f"\nReading PDF: {pdf_path}")
            print(f"Total Pages: {len(pdf)}")

            for page_number in range(len(pdf)):

                print(
                    f"\nProcessing Page {page_number + 1}"
                )

                try:

                    page = pdf.load_page(
                        page_number
                    )

                    print(
                        f"Page Rotation: {page.rotation}"
                    )

                    # First try normal PDF text extraction
                    page_text = page.get_text()

                    if page_text.strip():

                        full_text += "\n"
                        full_text += page_text

                        print(
                            f"Text Found Page {page_number + 1}"
                        )

                        print(
                            f"Characters Extracted: {len(page_text)}"
                        )

                    else:

                        print(
                            f"OCR Running Page {page_number + 1}"
                        )

                        pix = page.get_pixmap(
                            matrix=fitz.Matrix(2, 2)
                        )

                        image_bytes = pix.tobytes(
                            "png"
                        )

                        image = Image.open(
                            BytesIO(image_bytes)
                        )

                        ocr_text = (
                            pytesseract.image_to_string(
                                image
                            )
                        )

                        full_text += "\n"
                        full_text += ocr_text

                        print(
                            f"OCR Completed Page {page_number + 1}"
                        )
                        

                except Exception as page_error:

                    print(
                        f"OCR Error Page "
                        f"{page_number + 1}: "
                        f"{page_error}"
                    )

                    continue

            pdf.close()

            print(
                "\nPDF Processing Completed"
            )

            print("\n\n===== EXTRACTED TEXT =====")
            print(full_text[:2000])

            return full_text.strip()

        except Exception as e:

            print(
                f"PDF Extraction Error: {e}"
            )

            return ""