# ApplyWise AI — Product Blueprint

## Product Summary

ApplyWise AI is a résumé and job-description comparison application that helps
job seekers understand how their documented technical skills align with a role.

The application combines:

- PDF résumé text extraction
- AI-assisted structured information extraction
- Deterministic Python skill matching
- Transparent score calculation
- Side-by-side requirement comparison
- Optional user feedback collection

ApplyWise supports career decision-making. It does not make recruitment or hiring
decisions.

---

## Problem

Job descriptions often contain long and mixed requirements, including:

- Required technical skills
- Preferred technical skills
- Experience expectations
- Education requirements
- Domain knowledge
- Additional responsibilities

Job seekers may find it difficult to determine:

- Which skills from their résumé match the role
- Which important skills appear to be missing
- Whether requirements are required or preferred
- How their experience and education compare with the posting

ApplyWise organizes this information into a clearer, reviewable format.

---

## Target Users

ApplyWise is intended primarily for:

- Students
- Recent graduates
- Internship applicants
- Early-career professionals
- Career changers
- Job seekers reviewing technical roles

The current version is designed for individual self-assessment rather than
employer-side candidate screening.

---

## User Goal

A user should be able to:

1. Upload a text-based PDF résumé.
2. Paste a complete job description.
3. Run the comparison.
4. Review matched and missing required skills.
5. Review matched and missing preferred skills.
6. Understand how the technical score was calculated.
7. Compare experience and education information manually.
8. Review extracted domain knowledge.
9. Submit optional feedback.

---

## Core User Flow

```text
Open ApplyWise
      │
      ▼
Upload PDF Résumé
      │
      ▼
Paste Job Description
      │
      ▼
Validate Inputs
      │
      ▼
Extract PDF Text
      │
      ▼
Send Résumé and Job Text to Groq
      │
      ▼
Receive Structured Data
      │
      ▼
Normalize and Compare Skills in Python
      │
      ▼
Calculate Technical Skill Score
      │
      ▼
Display Results and Supporting Evidence
      │
      ▼
Optional Feedback Submission