import os


class FolderReader:

    def get_pdf_files(self, folder_path):

        pdf_files = []

        for file in os.listdir(folder_path):

            if file.lower().endswith(".pdf"):

                pdf_files.append(
                    os.path.join(folder_path, file)
                )

        return pdf_files