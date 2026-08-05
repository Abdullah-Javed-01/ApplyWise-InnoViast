# 🎯 ApplyWise AI

An AI-assisted résumé and job-description comparison application that helps users understand how their documented technical skills align with a job posting.

ApplyWise extracts structured information from both documents, applies deterministic Python skill-matching logic, and presents:

- A transparent technical-skill score
- Matched and missing required skills
- Matched and missing preferred skills
- Experience and education side-by-side comparisons
- Extracted domain-knowledge requirements

ApplyWise is a decision-support tool. It does not make hiring decisions or guarantee employment outcomes.

---

## Overview

ApplyWise AI was developed as part of the **AI Chatbot Developer Internship at INNOVIAST IT Solutions and Services**.

The application allows a user to:

1. Upload a text-based PDF résumé.
2. Paste a job description.
3. Extract structured information through the Groq API.
4. Compare technical skills using deterministic Python logic.
5. Review matched and missing required skills.
6. Review matched and missing preferred skills.
7. compare experience and education information side by side.
8. View domain knowledge extracted from the job description.
9. Submit optional feedback through Supabase.

The system is designed to support human review rather than replace it.

---

## Application Preview

![ApplyWise AI](docs/screenshots/testing/TC01%20%E2%80%94%20AI%20%26%20Machine%20Learning%20Engineer.png)

---

## Features

- PDF résumé upload
- Résumé text extraction with `pypdf`
- AI-assisted résumé information extraction
- AI-assisted job-description extraction
- Required and preferred skill separation
- Deterministic skill comparison
- Skill normalization and controlled aliases
- Transparent weighted technical-skill score
- Matched and missing required skills
- Matched and missing preferred skills
- Experience side-by-side comparison
- Education side-by-side comparison
- Domain-knowledge extraction
- Input validation
- Image-only PDF detection
- Groq API error and rate-limit handling
- Optional feedback collection
- Supabase feedback storage
- Responsive Streamlit interface
- Documented manual functional testing

---

## Technology Stack

### Application

- Python
- Streamlit
- Custom CSS

### AI Integration

- Groq API
- Structured prompt-based extraction
- JSON response parsing

### Document Processing

- `pypdf`

### Database

- Supabase

### Configuration

- `python-dotenv`
- Environment variables

---

## How It Works

```text
PDF Résumé
     │
     ▼
Text Extraction
     │
     ▼
Groq Résumé Extraction
     │
     ▼
Structured Candidate Data
     │
     ├───────────────────┐
     │                   │
     ▼                   ▼
Job Description     Groq Job Extraction
                         │
                         ▼
                 Structured Job Data
                         │
                         ▼
               Python Skill Comparison
                         │
                         ▼
              Score + Matching Evidence
```

### Processing Flow

1. The user uploads a text-based PDF résumé.
2. The application extracts readable text from the PDF.
3. The résumé extraction prompt converts the text into structured data.
4. The job-description prompt extracts structured job requirements.
5. Python normalizes and compares candidate skills with job skills.
6. Required and preferred skills are scored separately.
7. The final technical-skill score is calculated using the available skill groups.
8. Experience, education, and domain knowledge are displayed separately.
9. The user may submit optional feedback.

---

## Technical Skill Score

ApplyWise calculates a technical-skill score from the skills extracted from the résumé and job description.

Experience, education, domain knowledge, and other requirements are displayed separately and do not directly affect the technical-skill score.

### When Required and Preferred Skills Are Present

```text
Technical Skill Score =
(Required Skill Score × 0.80)
+
(Preferred Skill Score × 0.20)
```

### When Only Required Skills Are Present

```text
Technical Skill Score = Required Skill Score
```

### When Only Preferred Skills Are Present

```text
Technical Skill Score = Preferred Skill Score
```

### When No Skills Are Extracted

```text
Technical Skill Score = 0%
```

This logic prevents preferred-only job descriptions from being incorrectly capped at 20%.

### Score Interpretation

The technical score is an estimated comparison based on extracted résumé and job-description text.

It is not:

- An employer-issued score
- A complete measurement of candidate ability
- A hiring recommendation
- A prediction of interview selection
- A guarantee of selection or rejection

Users should manually review the matched and missing skills.

---

## Experience and Education Comparison

ApplyWise displays the candidate's extracted experience and education beside the corresponding job requirements.

The application does not automatically determine whether the candidate fully satisfies those requirements.

Users must review the comparison manually because:

- Experience may be described indirectly
- Education equivalencies may vary
- Employers may accept alternative qualifications
- AI-assisted extraction may miss or misinterpret information

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
│   ├── evaluation_report.md
│   └── test_cases.csv
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

## Local Setup

### 1. Clone the Repository

```powershell
git clone https://github.com/Abdullah-Javed-01/ApplyWise-InnoViast.git
cd ApplyWise-InnoViast
```

### 2. Create a Virtual Environment

```powershell
python -m venv .venv
```

### 3. Activate the Virtual Environment

#### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
.venv\Scripts\activate.bat
```

#### Linux or macOS

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Configure Environment Variables

Copy `.env.example` or create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_PUBLISHABLE_KEY=your_supabase_publishable_key
```

Never commit a real `.env` file or include it in a shared ZIP archive.

### 6. Run the Application

```powershell
python -m streamlit run app.py
```

Open the local address displayed by Streamlit, normally:

```text
http://localhost:8501
```

---

## Usage

1. Open the Streamlit application.
2. Upload a text-based PDF résumé.
3. Paste the complete job description.
4. Click **Analyze Match**.
5. Review:
   - Technical skill score
   - Matched required skills
   - Missing required skills
   - Matched preferred skills
   - Missing preferred skills
   - Experience comparison
   - Education comparison
   - Domain knowledge
6. Submit optional feedback when desired.

---

## Evaluation

ApplyWise passed all **10 planned manual functional test scenarios**.

The scenarios covered multiple job categories and application behaviours, including:

- Résumé extraction
- Job-description extraction
- Required and preferred skill comparison
- Experience and education display
- Domain-knowledge extraction
- Missing-input validation
- Image-only PDF handling
- Groq API rate-limit handling
- Feedback submission
- Supabase feedback storage

This result confirms that the tested workflows functioned as planned.

It does not represent:

- 100% résumé-extraction accuracy
- 100% skill-matching accuracy
- Employer-validated scoring
- Hiring-outcome accuracy

### Documented Test Roles

- AI & Machine Learning Engineer
- Data Scientist
- Data Analyst
- Business Analyst
- Associate Software Engineer — Python/Django
- Associate AI Engineer — Claude Certified Architect
- Associate Computer Vision Engineer
- Principal/Staff Machine Learning Engineer
- ML Engineer
- Senior AI Engineer

### Evaluation Resources

- [Evaluation Report](evaluation/evaluation_report.md)
- [Manual Test Cases](evaluation/test_cases.csv)
- [Testing Screenshots](docs/screenshots/testing/)
- [Functional Testing Report](docs/TESTING_REPORT.md)

The recorded screenshots and scores were produced during manual testing. Some values may differ when the application is rerun because AI-assisted extraction can vary.

---

## Validation Tests

The application was also checked for:

- Missing résumé
- Missing job description
- Image-only or scanned PDF
- Valid text-based PDF analysis
- Groq API rate-limit errors
- Feedback with comments
- Feedback without comments
- Supabase feedback storage
- Required and preferred skills together
- Required skills only
- Preferred skills only
- No extracted skills

---

## Privacy and Data Processing

ApplyWise processes résumé and job-description text through the configured Groq API.

This means the document text is sent to a third-party service for structured extraction. Groq's own data-processing and privacy policies apply.

The application does not intentionally store uploaded résumé files or complete job descriptions in Supabase.

Optional feedback may store:

- Rating
- Feedback comments
- Extracted job title
- Technical skill score
- Submission timestamp

Users should avoid uploading or entering unnecessary sensitive information, including:

- National identity numbers
- Passport details
- Banking information
- Passwords
- API keys
- Medical information
- Confidential employer information

Read:

- [Data Boundary and Privacy](docs/data_boundary.md)
- [Ethics and Responsible Use](docs/ethics.md)

---

## Responsible Use

ApplyWise is intended for personal career support and application review.

It should not be used to:

- Automatically accept or reject candidates
- Rank applicants for employment
- Make final hiring decisions
- Determine interview eligibility
- Infer protected or sensitive characteristics
- Replace recruiter or employer judgment

The system's results should always be reviewed against the original résumé and job description.

---

## Known Limitations

- Only PDF résumés are supported.
- PDFs must contain selectable text.
- OCR is not included for scanned or image-only PDFs.
- AI-assisted extraction may miss or misclassify information.
- Equivalent skills may not always be recognized.
- Skill matching depends on the extracted text.
- Experience and education are displayed but not automatically evaluated.
- The technical score does not measure soft skills, motivation, communication, or potential.
- Groq API availability and rate limits may affect analysis.
- Supabase availability may affect feedback submission.
- The application does not guarantee interviews or hiring outcomes.

Read more:

- [Known Limitations](KNOWN_LIMITATIONS.md)

---

## Documentation

Completed documentation:

- [Evaluation Report](evaluation/evaluation_report.md)
- [Manual Test Cases](evaluation/test_cases.csv)
- [Functional Testing Report](docs/TESTING_REPORT.md)
- [Data Boundary and Privacy](docs/data_boundary.md)
- [Ethics and Responsible Use](docs/ethics.md)
- [Learning Journal](LEARNING_JOURNAL.md)
- [Changelog](CHANGELOG.md)
- [Known Limitations](KNOWN_LIMITATIONS.md)

Additional documentation files should only be linked publicly after their contents are completed.

---

## Future Improvements

- OCR support for scanned résumés
- DOCX résumé support
- Expanded synonym and alias handling
- Skill-category grouping
- Résumé-improvement suggestions
- Learning recommendations
- Cover-letter generation
- Downloadable analysis reports
- User accounts and analysis history
- Analytics dashboard
- Multiple-résumé comparison
- Interview-preparation support
- Automated unit tests
- Reusable job-description test fixtures
- Ground-truth extraction evaluation

---

## Security

Credentials must be stored in `.env` or Streamlit secrets.

Never commit or share:

- `GROQ_API_KEY`
- Supabase service-role keys
- Database passwords
- `.env`
- `.venv/`
- `.git/`

The Supabase feedback table should use Row Level Security and minimum required permissions.

---

## Disclaimer

ApplyWise provides an estimated comparison based only on the uploaded résumé and pasted job description.

It does not guarantee:

- Selection
- Rejection
- Interview eligibility
- Employment
- Hiring outcomes

Users should review all results carefully and use their own judgment before making application or career decisions.

---

## Author

**Abdullah Javed**

AI Chatbot Developer Intern  
INNOVIAST IT Solutions and Services

- GitHub: [Abdullah-Javed-01](https://github.com/Abdullah-Javed-01)
- LinkedIn: [Abdullah Javed](https://www.linkedin.com/in/abdullah-javed-id01)

---

## Version

**ApplyWise AI v1.0**

Developed in August 2026.