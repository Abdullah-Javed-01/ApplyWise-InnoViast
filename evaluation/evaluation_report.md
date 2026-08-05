# ApplyWise AI — Evaluation Report

## Scope

This report documents the evaluation activities completed for ApplyWise AI.

The project currently includes:

- Repeated-input stability testing
- Ten documented manual functional test scenarios
- Validation testing for missing and unsupported inputs
- Screenshot evidence for the manual test scenarios

This is not an automated benchmark of résumé-extraction accuracy, hiring accuracy,
or employer decision quality.

---

## Repeated-Input Evaluation

The same résumé and job description were analyzed more than once to examine
consistency.

### Initial issue: equivalent skill wording

Exact text comparison initially treated semantically equivalent skills as
different.

Example:

- Résumé: `Retrieval-Augmented Generation (RAG)`
- Job description: `Retrieval Augmented Generation (RAG)`

### Improvement

The scoring logic was improved using:

- Skill normalization
- Skill aliases
- Controlled evidence rules
- Deterministic Python comparison

---

### Initial issue: extraction variation

The AI extraction step sometimes returned a different number of skills from the
same long job description.

### Improvement

The Groq extraction configuration was changed to:

```python
temperature=0.0