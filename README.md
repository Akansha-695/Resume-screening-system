# AI Resume Screening System

A Python + Streamlit application that screens a batch of résumés (PDF/DOCX) against a Job Description (JD) and ranks candidates by how well they match the job requirements.

## How It Works

1. **Paste a Job Description** into the text area.
2. **Upload one or more résumés** (PDF or DOCX format only).
3. Click **"Screen Resumes"** — the system will:
   - Parse the JD to identify required information
   - Extract text from each uploaded résumé
   - Extract skills from the résumé text using a predefined skills taxonomy
   - Calculate a match score for each candidate
4. View a **ranked table** of candidates sorted by score (highest first), including their matched skills.

## Project Structure

```
Resume-screening-system/
├── app.py                        # Streamlit web interface (entry point)
├── parsers/
│   ├── resume_parser.py          # Extracts text from PDF/DOCX résumés
│   └── jd_parser.py              # Parses the job description
├── extractors/
│   └── keyword_extractor.py      # Matches résumé text against skills taxonomy
├── matcher/
│   └── scorer.py                 # Calculates the candidate match score
├── data/
│   └── skills_taxonomy.json      # Skills database used for keyword matching
└── requirements.txt               # Python dependencies
```

## Requirements

- Python 3.9+
- Dependencies listed in `requirements.txt` (installed via pip — see below)

Key libraries used:
- `streamlit` — web interface
- `PyPDF2` — PDF text extraction
- `python-docx` / `docx2txt` — DOCX text extraction
- `pandas` — results table and ranking

## Installation

```bash
git clone https://github.com/Akansha-695/Resume-screening-system.git
cd Resume-screening-system
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

## Running the App

```bash
streamlit run app.py
```

The app will open in your browser (typically at `http://localhost:8501`).

## Usage

1. Paste the job description text into the **"Paste Job Description"** box.
2. Upload one or more résumés using the file uploader (**PDF or DOCX only** — other formats will be rejected).
3. Click **"Screen Resumes"**.
4. Review the ranked candidate table, showing:
   - **Name** — the uploaded file name
   - **Score** — the calculated match score
   - **Skills** — the skills matched against the job description

## Known Limitations

- Only PDF and DOCX résumé formats are supported; other formats (e.g. `.txt`, `.doc`) are rejected.
- Skill matching depends on the predefined taxonomy in `data/skills_taxonomy.json` — skills not listed there will not be detected.

## Future Improvements

- Add a command-line interface for batch processing without the web UI.
- Expand the skills taxonomy for broader domain coverage.
- Add experience-level and keyword-frequency scoring components.
- Export ranked results to CSV/PDF report.

## Author

Akansha Kashyap
