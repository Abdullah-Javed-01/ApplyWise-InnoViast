import re


SKILL_ALIASES = {
    "retrieval augmented generation rag": "rag",
    "retrieval augmented generation": "rag",
    "rag": "rag",

    "scikit learn": "scikit-learn",
    "sklearn": "scikit-learn",

    "large language models": "llms",
    "large language model": "llms",
    "llm": "llms",
    "llms": "llms",

    "generative ai models": "generative-ai",
    "generative ai": "generative-ai",
    "gen ai": "generative-ai",

    "open source llms": "open-source-llms",
    "open source large language models": "open-source-llms",
}


EVIDENCE_RULES = {
    "open-source-llms": {
        "ollama",
        "llama 3 2",
        "gemma 3",
        "qwen2 5",
    },
    "generative-ai": {
        "llms",
        "ollama",
        "llama 3 2",
        "gemma 3",
        "qwen2 5",
        "prompt engineering",
        "rag",
    },
}


def normalize_skill(skill: str) -> str:
    normalized = skill.strip().lower()

    normalized = re.sub(r"[^a-z0-9+#]+", " ", normalized)
    normalized = " ".join(normalized.split())

    return SKILL_ALIASES.get(normalized, normalized)

def calculate_skill_match(candidate_skills, job_skills):
    candidate_skill_set = {
        normalize_skill(skill)
        for skill in candidate_skills
    }

    matched_skills = []
    missing_skills = []
    seen_job_skills = set()

    for original_job_skill in job_skills:
        normalized_job_skill = normalize_skill(original_job_skill)

        # Avoid counting duplicate job skills
        if normalized_job_skill in seen_job_skills:
            continue

        seen_job_skills.add(normalized_job_skill)

        if normalized_job_skill in candidate_skill_set:
            matched_skills.append(original_job_skill)
            continue

        supporting_skills = EVIDENCE_RULES.get(
            normalized_job_skill,
            set(),
        )

        if candidate_skill_set & supporting_skills:
            matched_skills.append(original_job_skill)
        else:
            missing_skills.append(original_job_skill)

    total_job_skills = len(seen_job_skills)

    if total_job_skills:
        score = (
            len(matched_skills)
            / total_job_skills
        ) * 100
    else:
        score = 0

    return (
        matched_skills,
        missing_skills,
        round(score, 2),
    )

def calculate_weighted_skill_score(
    required_score: float,
    preferred_score: float,
    required_skills: list[str],
    preferred_skills: list[str],
) -> float:
    """Calculate the final technical score based on available skill groups."""

    has_required_skills = bool(required_skills)
    has_preferred_skills = bool(preferred_skills)

    if has_required_skills and has_preferred_skills:
        final_score = (
            required_score * 0.80
            + preferred_score * 0.20
        )

    elif has_required_skills:
        final_score = required_score

    elif has_preferred_skills:
        final_score = preferred_score

    else:
        final_score = 0.0

    return round(final_score, 1)