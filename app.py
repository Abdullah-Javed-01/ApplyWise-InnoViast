from pathlib import Path

import streamlit as st

from utils.feedback_service import save_feedback
from utils.groq_client import ask_groq
from utils.parser import parse_json_response
from utils.pdf_reader import extract_text_from_pdf
from utils.scoring import calculate_skill_match
from utils.ui import (
    display_brand_header,
    display_comparison_card,
    display_domain_tags,
    display_empty_state,
    display_feedback_form,
    display_skill_tags,
    display_success_message,
    display_summary_cards,
    inject_custom_css,
)


BASE_DIR = Path(__file__).resolve().parent
DEVELOPER_MODE = False


def remove_duplicate_skills(
    skills: list[str],
) -> list[str]:
    """Remove duplicate skills while preserving their original order."""

    unique_skills = []
    seen_skills = set()

    for skill in skills:
        cleaned_skill = str(skill).strip()
        comparison_value = cleaned_skill.lower()

        if cleaned_skill and comparison_value not in seen_skills:
            unique_skills.append(cleaned_skill)
            seen_skills.add(comparison_value)

    return unique_skills


st.set_page_config(
    page_title="ApplyWise AI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_custom_css()
display_brand_header()


input_column, result_column = st.columns(
    [0.9, 1.8],
    gap="medium",
)


with input_column:
    with st.container(border=True):
        st.markdown("### 📄 Job Details")

        resume_file = st.file_uploader(
            "Upload your résumé",
            type=["pdf"],
            help=(
                "Upload a PDF résumé containing selectable text. "
                "Scanned image-only PDFs are not supported in Version 1."
            ),
        )

        job_description = st.text_area(
            "Paste the job description",
            placeholder="Paste the complete job description here...",
            height=280,
        )

        analyze_button = st.button(
            "✨ Analyze Match",
            type="primary",
            use_container_width=True,
        )


with result_column:
    if not analyze_button:
        display_empty_state()


if analyze_button:
    if resume_file is None:
        with result_column:
            st.error(
                "Please upload your résumé before starting the analysis."
            )

    elif not job_description.strip():
        with result_column:
            st.error(
                "Please paste a job description before starting the analysis."
            )

    else:
        try:
            with result_column:
                progress_message = st.empty()

            progress_message.info("📄 Reading your résumé...")

            resume_text = extract_text_from_pdf(resume_file)

            if not resume_text:
                progress_message.empty()

                with result_column:
                    st.error(
                        "No readable text was found in this PDF. "
                        "Please upload a résumé containing selectable text."
                    )

                st.stop()

            resume_prompt_path = (
                BASE_DIR
                / "prompts"
                / "resume_extraction_prompt.txt"
            )

            resume_prompt_template = resume_prompt_path.read_text(
                encoding="utf-8"
            )

            final_resume_prompt = resume_prompt_template.replace(
                "{resume_text}",
                resume_text,
            )

            progress_message.info(
                "🤖 Extracting résumé information..."
            )

            resume_ai_response = ask_groq(
                final_resume_prompt
            )

            candidate_data = parse_json_response(
                resume_ai_response
            )

            job_prompt_path = (
                BASE_DIR
                / "prompts"
                / "job_extraction_prompt.txt"
            )

            job_prompt_template = job_prompt_path.read_text(
                encoding="utf-8"
            )

            final_job_prompt = job_prompt_template.replace(
                "{job_description}",
                job_description,
            )

            progress_message.info(
                "📋 Understanding the job description..."
            )

            job_ai_response = ask_groq(
                final_job_prompt
            )

            job_data = parse_json_response(
                job_ai_response
            )

            progress_message.info(
                "📊 Comparing technical skills..."
            )

            (
                required_matched,
                required_missing,
                required_score,
            ) = calculate_skill_match(
                candidate_data.get("skills", []),
                job_data.get("required_skills", []),
            )

            (
                preferred_matched,
                preferred_missing,
                preferred_score,
            ) = calculate_skill_match(
                candidate_data.get("skills", []),
                job_data.get("preferred_skills", []),
            )

            if job_data.get("preferred_skills"):
                technical_skill_score = round(
                    (required_score * 0.80)
                    + (preferred_score * 0.20),
                    1,
                )
            else:
                technical_skill_score = round(
                    required_score,
                    1,
                )

            matched_skills = remove_duplicate_skills(
                required_matched + preferred_matched
            )

            missing_skills = remove_duplicate_skills(
                required_missing + preferred_missing
            )

            candidate_name = (
                candidate_data
                .get("name", "")
                .strip()
                .title()
            )

            job_title = (
                job_data
                .get("job_title", "")
                .strip()
            )

            experience_requirements = (
                job_data.get("required_experience", [])
                + job_data.get("preferred_experience", [])
            )

            domain_knowledge = job_data.get(
                "domain_knowledge",
                [],
            )

            progress_message.empty()

            with result_column:
                display_success_message()

                identity_parts = []

                if candidate_name:
                    identity_parts.append(
                        f"Candidate: {candidate_name}"
                    )

                if job_title:
                    identity_parts.append(
                        f"Role: {job_title}"
                    )

                if identity_parts:
                    st.markdown(
                        f"**{' · '.join(identity_parts)}**"
                    )

                display_summary_cards(
                    score=technical_skill_score,
                    matched_count=len(matched_skills),
                    missing_count=len(missing_skills),
                )

                skill_left, skill_right = st.columns(
                    2,
                    gap="small",
                )

                with skill_left:
                    display_skill_tags(
                        title="Matched Skills",
                        skills=matched_skills,
                        matched=True,
                    )

                with skill_right:
                    display_skill_tags(
                        title="Missing Skills",
                        skills=missing_skills,
                        matched=False,
                    )

                comparison_left, comparison_right = st.columns(
                    2,
                    gap="small",
                )

                with comparison_left:
                    display_comparison_card(
                        title="Experience Comparison",
                        icon="💼",
                        candidate_label="Your Experience",
                        candidate_items=candidate_data.get(
                            "experience",
                            [],
                        ),
                        required_label="Required Experience",
                        required_items=experience_requirements,
                    )

                with comparison_right:
                    display_comparison_card(
                        title="Education Comparison",
                        icon="🎓",
                        candidate_label="Your Education",
                        candidate_items=candidate_data.get(
                            "education",
                            [],
                        ),
                        required_label="Required Education",
                        required_items=job_data.get(
                            "education_requirements",
                            [],
                        ),
                    )

            display_domain_tags(
                domain_knowledge
            )

            display_feedback_form(
                job_title=job_title,
                technical_skill_score=technical_skill_score,
                save_feedback_function=save_feedback,
            )

            st.caption(
                "ApplyWise AI provides an estimated comparison based "
                "only on the uploaded résumé and pasted job description. "
                "It does not guarantee selection, rejection, interview "
                "eligibility, or hiring outcomes. AI extraction may "
                "occasionally miss or classify information incorrectly. "
                "Review the results carefully and use your own judgment "
                "before making an application decision."
            )

            if DEVELOPER_MODE:
                with st.expander("Developer details"):
                    st.markdown("### Candidate data")
                    st.json(candidate_data)

                    st.markdown("### Job data")
                    st.json(job_data)

                    st.markdown("### Score breakdown")
                    st.json(
                        {
                            "required_skill_score": required_score,
                            "preferred_skill_score": preferred_score,
                            "technical_skill_score": technical_skill_score,
                        }
                    )

        except FileNotFoundError as error:
            with result_column:
                st.error(
                    "A required application file could not be found. "
                    "Please contact the application owner."
                )

                if DEVELOPER_MODE:
                    st.code(str(error))

        except ValueError as error:
            with result_column:
                st.error(
                    f"The analysis could not be completed: {error}"
                )

        except Exception as error:
            with result_column:
                st.error(
                    "Something went wrong while analyzing the résumé "
                    "and job description. Please try again."
                )

                if DEVELOPER_MODE:
                    with st.expander("Technical details"):
                        st.code(str(error))