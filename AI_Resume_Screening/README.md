# AI Resume Screening

A Streamlit application that screens candidate resumes against a job description by extracting skills and computing a compatibility score.

## Features

- Upload PDF or DOCX resumes
- Extract text from documents
- Detect common technical skills
- Match skills against a job description
- Score and rank candidates

## Tech Stack

- Python
- Streamlit
- PyMuPDF
- python-docx
- Pytest

## Setup

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

## Testing

```bash
python -m pytest -q
```

## Example

The app includes a sample job description and candidate ranking section to demonstrate the screening flow.
