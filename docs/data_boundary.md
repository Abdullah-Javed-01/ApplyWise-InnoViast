# ApplyWise AI — Data Boundary and Privacy

## Purpose

ApplyWise AI compares an uploaded résumé with a pasted job description to help
users understand skill alignment, missing requirements, experience expectations,
and education requirements.

The output is informational only and must not be treated as a hiring decision.

## Data Provided by the User

ApplyWise may process:

- Résumé PDF files
- Extracted résumé text
- Job-description text
- Optional feedback rating
- Optional feedback comments

Users should avoid including unnecessary sensitive information such as:

- National identity numbers
- Passport numbers
- Banking information
- Passwords
- API keys
- Medical information
- Other confidential credentials

## Data Processing

### Résumé and Job Description

Résumé text and job-description text are sent to the configured Groq API for
structured extraction.

The extracted information may include:

- Candidate name
- Skills
- Experience
- Education
- Required skills
- Preferred skills
- Job title
- Experience requirements
- Education requirements
- Domain knowledge

Groq is a third-party service. Its own privacy, processing, and retention policies
apply to data sent through its API.

## Local Application Behaviour

ApplyWise processes uploaded PDF files during the active Streamlit session.

The application does not intentionally save uploaded résumé files or complete job
descriptions to the project repository.

Temporary data may remain in application memory while the session is active.

## Feedback Storage

When a user submits feedback, ApplyWise may store the following in Supabase:

- Rating
- Optional comments
- Extracted job title
- Technical skill score
- Submission timestamp

Uploaded résumé files and complete job descriptions are not intentionally stored
in the feedback table.

Supabase is a third-party service. Its own privacy, security, and retention
policies apply.

## Credentials

API keys and database credentials must be stored in environment variables or
Streamlit secrets.

They must never be:

- Hard-coded in source files
- Committed to Git
- Included in screenshots
- Shared inside public ZIP files
- Printed in logs or error messages

## Access Control

The Supabase feedback table should use Row Level Security policies that allow only
the minimum operations required by the application.

Administrative or service-role credentials must never be exposed in client-facing
code.

## Limitations

ApplyWise uses AI-assisted extraction and deterministic skill matching.

The system may:

- Miss relevant résumé evidence
- Misclassify a skill
- Interpret job requirements incorrectly
- Produce incomplete structured information
- Generate a score that does not reflect an employer's actual evaluation process

Users should review all results manually before making application or career
decisions.

## User Responsibility

By using ApplyWise, users are responsible for ensuring that they have permission
to process the uploaded documents and that the information does not violate any
privacy, employment, confidentiality, or organizational policies.