## Early Repeated-Input Evaluation

The same résumé and job description were analyzed repeatedly.

### Failure pattern 1
Exact text comparison incorrectly marked equivalent skills as missing.

Example:
- Résumé: Retrieval-Augmented Generation (RAG)
- Job: Retrieval Augmented Generation (RAG)

### Improvement
Added skill normalization, aliases, and controlled evidence rules.

### Failure pattern 2
The AI extracted different numbers of skills from the same long job description across repeated runs.

### Improvement
Set model temperature to 0 and added a final completeness-check instruction to the extraction prompt.

### Result
The final repeated tests produced weighted skill scores of 48.92% and 48.00%. The small difference confirms that the result should be presented as an estimate rather than an exact hiring prediction.