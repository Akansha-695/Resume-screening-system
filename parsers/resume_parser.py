from pathlib import Path
import PyPDF2
import docx2txt


class ResumeParser:

    def extract_text(self, file_path):

        file_path = Path(file_path)

        # PDF files
        if file_path.suffix.lower() == ".pdf":
            return self._extract_pdf(file_path)

        # DOCX files
        elif file_path.suffix.lower() == ".docx":
            return self._extract_docx(file_path)

        # TXT files
        elif file_path.suffix.lower() == ".txt":
            return file_path.read_text(
                encoding="utf-8"
            )

        return ""

    def _extract_pdf(self, file_path):

        text = ""

        with open(file_path, "rb") as file:

            pdf_reader = PyPDF2.PdfReader(file)

            for page in pdf_reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text.strip()

    def _extract_docx(self, file_path):

        text = docx2txt.process(file_path)

        return text.strip()