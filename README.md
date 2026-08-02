# 🎯 ApplyWise AI

An AI-powered résumé and job description matching application that helps users understand how well their résumé aligns with a job posting.

ApplyWise AI analyzes technical skills, experience, education, and domain knowledge, then presents an explainable technical match score with matched and missing skills.

---

## Overview

ApplyWise AI was developed as part of the **AI Chatbot Developer Internship at Innoviast IT Solutions and Services**.

The application allows a user to:

1. Upload a PDF résumé.
2. Paste a job description.
3. Extract structured information from both documents.
4. Compare technical skills using deterministic Python logic.
5. Review matched and missing skills.
6. Compare experience and education requirements.
7. View domain knowledge mentioned in the job description.
8. Submit anonymous feedback stored in Supabase.

The system is designed to support decision-making, not replace human judgment.

---

## Application Preview

![ApplyWise AI](docs/screenshots/testing/TC01%20%E2%80%94%20AI%20%26%20Machine%20Learning%20Engineer.png)

---

## Features

- PDF résumé upload
- Résumé text extraction
- AI-assisted résumé information extraction
- AI-assisted job description extraction
- Required and preferred skill separation
- Deterministic technical skill matching
- Weighted technical match score
- Matched skills display
- Missing skills display
- Experience comparison
- Education comparison
- Domain knowledge extraction
- Anonymous user feedback
- Supabase feedback storage
- Input validation
- Friendly error handling
- Responsive Streamlit interface
- Documented functional testing

---

## Tech Stack

### Frontend

- Streamlit
- Custom CSS

### Backend

- Python

### AI

- Groq API
- Structured prompt-based extraction

### Database

- Supabase

### Main Libraries

- Streamlit
- python-dotenv
- PyPDF
- Supabase Python client
- Groq Python client

---

## How It Works

```text
PDF Résumé
     │
     ▼
Text Extraction
     │
     ▼
AI Résumé Extraction
     │
     ▼
Structured Candidate Data
     │
     ├───────────────┐
     │               │
     ▼               ▼
Job Description   AI Job Extraction
                     │
                     ▼
              Structured Job Data
                     │
                     ▼
            Python Skill Comparison
                     │
                     ▼
             Match Score + Evidence
```

### Processing Flow

1. The user uploads a text-based PDF résumé.
2. The application extracts readable text from the file.
3. The résumé prompt converts the résumé into structured JSON.
4. The job description prompt extracts structured job requirements.
5. Python normalizes and compares candidate skills with job skills.
6. Required skills and preferred skills are scored separately.
7. The final technical score is calculated.
8. Experience, education, and domain knowledge are displayed separately.
9. The user can submit anonymous feedback.

---

## Scoring Approach

ApplyWise AI scores technical skills only.

Experience, education, domain knowledge, and other job requirements are shown separately and do not directly affect the technical skill score.

When preferred skills are available:

```text
Technical Skill Score =
(Required Skill Score × 0.80)
+
(Preferred Skill Score × 0.20)
```

When no preferred skills are listed:

```text
Technical Skill Score = Required Skill Score
```

This keeps the scoring transparent and avoids mixing unrelated factors into one number.

---

## Project Structure

```text
ApplyWise-InnoViast/
│
├── app.py
├── requirements.txt
├── README.md
├── CHANGELOG.md
├── KNOWN_LIMITATIONS.md
├── AI_USAGE.md
├── LEARNING_JOURNAL.md
├── .env.example
├── .gitignore
│
├── assets/
│
├── docs/
│   ├── data_boundary.md
│   ├── decisions.md
│   ├── ethics.md
│   ├── product_blueprint.md
│   ├── TESTING_REPORT.md
│   └── screenshots/
│       └── testing/
│
├── evaluation/
│
├── prompts/
│   ├── resume_extraction_prompt.txt
│   └── job_extraction_prompt.txt
│
└── utils/
    ├── __init__.py
    ├── feedback_service.py
    ├── groq_client.py
    ├── parser.py
    ├── pdf_reader.py
    ├── scoring.py
    └── ui.py
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Abdullah-Javed-01/ApplyWise-InnoViast.git
cd ApplyWise-InnoViast
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

#### Linux or macOS

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_PUBLISHABLE_KEY=your_supabase_publishable_key
```

Do not commit your real `.env` file.

### 6. Run the application

```bash
streamlit run app.py
```

---

## Usage

1. Open the application.
2. Upload a text-based PDF résumé.
3. Paste the complete job description.
4. Click **Analyze Match**.
5. Review:
   - Technical skill score
   - Matched skills
   - Missing skills
   - Experience comparison
   - Education comparison
   - Domain knowledge
6. Submit optional feedback.

---

## Functional Testing

ApplyWise AI was tested against ten different job categories:

- AI & Machine Learning Engineer
- Data Scientist
- Data Analyst
- Business Analyst
- Associate Software Engineer
- Associate AI Engineer
- Associate Computer Vision Engineer
- Principal/Staff Machine Learning Engineer
- ML Engineer
- Senior AI Engineer

All planned functional test cases passed.

Read the complete report:

- [Functional Testing Report](docs/TESTING_REPORT.md)

---

## Validation Tests

The application was also tested for:

- Missing résumé
- Missing job description
- Image-only PDF
- Valid PDF analysis
- Feedback with comments
- Feedback without comments
- Supabase feedback storage

---

## Known Limitations

- Only PDF résumés are supported.
- PDFs must contain selectable text.
- Image-only or scanned résumés are not supported.
- AI extraction may occasionally miss or classify information incorrectly.
- Skill matching depends on extracted terms.
- Equivalent skills may not always be recognized unless worded similarly.
- The technical score does not include experience or education.
- The application does not guarantee interview or hiring outcomes.

Read more:

- [Known Limitations](KNOWN_LIMITATIONS.md)

---

## Documentation

- [Product Blueprint](docs/product_blueprint.md)
- [Design Decisions](docs/decisions.md)
- [Ethics](docs/ethics.md)
- [Data Boundary](docs/data_boundary.md)
- [Functional Testing Report](docs/TESTING_REPORT.md)
- [AI Usage](AI_USAGE.md)
- [Learning Journal](LEARNING_JOURNAL.md)
- [Changelog](CHANGELOG.md)
- [Known Limitations](KNOWN_LIMITATIONS.md)

---

## Future Improvements

- OCR support for scanned résumés
- DOCX résumé support
- Improved synonym handling
- Skill-category grouping
- Resume improvement suggestions
- Learning recommendations
- Cover letter generation
- Downloadable analysis reports
- User accounts and analysis history
- Analytics dashboard
- Multiple résumé comparison
- Interview preparation support

---

## Privacy and Ethics

ApplyWise AI processes only the résumé and job description provided by the user.

The application does not claim to make hiring decisions. It provides an estimated comparison to help users understand alignment with job requirements.

Feedback is stored anonymously for product improvement.

---

## Disclaimer

ApplyWise AI provides an estimated comparison based only on the uploaded résumé and pasted job description.

It does not guarantee:

- Selection
- Rejection
- Interview eligibility
- Hiring outcomes

Users should review the results carefully and use their own judgment before making application decisions.

---

## Author

**Abdullah Javed**

AI Chatbot Developer Intern  
Innoviast IT Solutions and Services

- GitHub: [Abdullah-Javed-01](https://github.com/Abdullah-Javed-01)
- LinkedIn: [Abdullah Javed](https://www.linkedin.com/in/abdullah-javed-id01)

---

## Version

**ApplyWise AI v1.0**

Developed in August 2026.