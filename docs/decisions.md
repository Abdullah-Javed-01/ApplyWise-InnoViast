# ApplyWise AI — Design Decisions

This document records the main technical and product decisions made while developing ApplyWise AI.

---

## 1. Streamlit for the User Interface

### Decision

Use Streamlit as the application framework.

### Reason

Streamlit provides:

- Fast development with Python
- Native file-upload support
- Simple form and feedback components
- Easy display of scores, matched skills, and comparison sections
- Straightforward local and cloud deployment

### Trade-off

Streamlit is suitable for the current single-user workflow but provides less control than a custom frontend and backend architecture.

---

## 2. PDF as the Initial Résumé Format

### Decision

Support text-based PDF résumés in the first version.

### Reason

PDF is commonly used for résumés and can be processed directly with `pypdf`.

### Limitation

The current implementation does not support:

- Scanned or image-only PDFs
- OCR
- DOCX files
- Images
- Handwritten documents

A PDF must contain selectable text.

---

## 3. Groq for Structured Extraction

### Decision

Use the Groq API to extract structured information from résumé and job-description text.

### Reason

Résumés and job descriptions vary greatly in wording and structure. A language model can convert this unstructured text into fields such as:

- Skills
- Experience
- Education
- Required skills
- Preferred skills
- Job title
- Domain knowledge

### Configuration

Structured extraction uses:

```python
temperature=0.0
```

This reduces unnecessary output variation.

### Limitation

The same input may still occasionally produce different or incomplete structured results.

---

## 4. Separate Extraction from Scoring

### Decision

Use the language model for information extraction, but calculate the final technical score with Python.

### Reason

A deterministic scoring function is:

- Easier to explain
- Easier to test
- More consistent
- More transparent
- Less dependent on model wording

The language model does not directly decide the final score.

---

## 5. Separate Required and Preferred Skills

### Decision

Extract and score required and preferred skills separately.

### Reason

Required skills and preferred skills do not normally have equal importance in a job description.

Separating them helps users understand:

- Which skills are essential
- Which skills are optional advantages
- Where the most important gaps exist

---

## 6. Weighted Technical Score

### Decision

When both required and preferred skills are present, use:

```text
Final Score =
(Required Skill Score × 0.80)
+
(Preferred Skill Score × 0.20)
```

### Reason

Required skills receive greater weight because they are presented as the primary technical expectations.

### Additional Rules

When only required skills are present:

```text
Final Score = Required Skill Score
```

When only preferred skills are present:

```text
Final Score = Preferred Skill Score
```

When no skills are extracted:

```text
Final Score = 0%
```

### Correction

The original implementation incorrectly limited preferred-only roles to a maximum score of 20%.

The scoring logic was updated so the available skill group determines the full score when only one group exists.

---

## 7. Technical Skills Only in the Score

### Decision

Do not include experience, education, domain knowledge, or soft skills in the technical score.

### Reason

Combining unrelated factors into one number would make the result difficult to interpret and could create misleading assumptions.

The displayed score represents only extracted technical-skill alignment.

---

## 8. Manual Experience and Education Review

### Decision

Display candidate and job information side by side instead of automatically deciding eligibility.

### Reason

Experience and education requirements often require human interpretation.

For example:

- Equivalent degrees may be accepted
- Relevant projects may partly substitute for formal experience
- Experience duration may be described indirectly
- Employers may accept alternative qualifications

ApplyWise therefore presents the information without automatically declaring that the candidate qualifies or does not qualify.

---

## 9. Skill Normalization and Aliases

### Decision

Normalize skill text and use controlled aliases during comparison.

### Reason

The same skill can appear in different forms, such as:

- `RAG`
- `Retrieval-Augmented Generation`
- `Retrieval Augmented Generation`

Controlled aliases reduce false mismatches without allowing unsupported evidence.

### Trade-off

The alias list is not exhaustive. Some equivalent skills may still be missed.

---

## 10. Evidence-Based Matching

### Decision

Match a job skill only when supported by extracted résumé evidence or an approved alias.

### Reason

The application should not assume that a candidate possesses a skill merely because it is related to another technology.

This reduces unsupported matches and makes the score easier to explain.

---

## 11. Supabase for Optional Feedback

### Decision

Use Supabase to store optional user feedback.

### Stored Information

Feedback may include:

- Rating
- Optional comments
- Extracted job title
- Technical score
- Submission timestamp

### Data Boundary

The application does not intentionally store complete résumé files or full job descriptions in the feedback table.

### Security Requirement

The Supabase table should use Row Level Security and only the minimum permissions required by the application.

---

## 12. Environment Variables for Credentials

### Decision

Store credentials in `.env` files or Streamlit secrets.

### Protected Values

Examples include:

- `GROQ_API_KEY`
- `SUPABASE_URL`
- `SUPABASE_PUBLISHABLE_KEY`

### Rule

Real credentials must never be:

- Hard-coded
- Committed to Git
- Included in screenshots
- Included in shared ZIP files
- Printed in logs

The repository includes `.env.example` for configuration guidance.

---

## 13. Friendly Error Handling

### Decision

Display understandable messages for common failures.

### Covered Cases

- Missing résumé
- Missing job description
- Empty PDF text
- Image-only PDF
- Invalid model response
- Groq authentication error
- Groq rate-limit error
- Groq service failure
- Feedback-storage failure

### Reason

Users should understand what happened without being exposed to unnecessary technical details or secret values.

---

## 14. Manual Functional Testing

### Decision

Document ten role-based manual functional test scenarios.

### Reason

The tests provide evidence that the complete workflow functions across multiple job categories.

### Scope

The test result means:

> All 10 planned manual functional test scenarios passed.

It does not mean:

- 100% extraction accuracy
- 100% matching accuracy
- Employer-validated scoring
- Hiring-outcome accuracy

Further details are available in:

- [Evaluation Report](../evaluation/evaluation_report.md)
- [Manual Test Cases](../evaluation/test_cases.csv)
- [Functional Testing Report](TESTING_REPORT.md)

---

## 15. Decision-Support Positioning

### Decision

Position ApplyWise as a job-seeker support tool rather than a hiring system.

### Reason

The application is designed to help users review their own résumé alignment.

It should not:

- Rank candidates
- Accept or reject applicants
- Determine interview eligibility
- Make final hiring decisions
- Infer protected characteristics
- Replace human judgment

---

## Future Decisions to Revisit

The following may require new design decisions in later versions:

- OCR for scanned résumés
- DOCX support
- Downloadable reports
- User accounts
- Analysis history
- Improved skill ontology
- Ground-truth extraction evaluation
- Automated unit tests
- Résumé-improvement suggestions
- Multiple-résumé comparison
- Employer-facing workflows