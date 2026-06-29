from app.tools.folder_reader import FolderReader


reader = FolderReader()

files = reader.get_pdf_files(
    "uploads"
)

print(files)