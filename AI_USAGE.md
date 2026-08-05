# ApplyWise AI — AI Usage

## Purpose

ApplyWise uses a language model to convert unstructured résumé and job-description
text into structured information.

The language model supports information extraction only. It does not make hiring
decisions or calculate the final technical-skill score.

---

## Runtime AI Service

ApplyWise uses the Groq API through the Groq Python client.

The configured model receives:

- Extracted résumé text
- Pasted job-description text
- Structured extraction instructions

The model returns structured information such as:

### Résumé Information

- Candidate name
- Technical skills
- Experience
- Education

### Job-Description Information

- Job title
- Required skills
- Preferred skills
- Experience requirements
- Education requirements
- Domain knowledge

The extraction temperature is configured as:

```python
temperature=0.0