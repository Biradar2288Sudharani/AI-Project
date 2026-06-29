from app.tools.pdf_reader import PDFReader

pdf_path = r"uploads\patient 1.pdf"

text = PDFReader.extract_text(pdf_path)

print(text[:5000])