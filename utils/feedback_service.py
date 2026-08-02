from pathlib import Path
import os

from dotenv import load_dotenv
from supabase import Client, create_client


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


def get_setting(name: str) -> str | None:
    value = os.getenv(name)

    if value:
        return value

    try:
        import streamlit as st

        return st.secrets.get(name)
    except Exception:
        return None


def get_supabase_client() -> Client:
    supabase_url = get_setting("SUPABASE_URL")
    publishable_key = get_setting("SUPABASE_PUBLISHABLE_KEY")

    if not supabase_url:
        raise ValueError(
            "SUPABASE_URL was not found in .env or Streamlit secrets."
        )

    if not publishable_key:
        raise ValueError(
            "SUPABASE_PUBLISHABLE_KEY was not found in .env "
            "or Streamlit secrets."
        )

    return create_client(
        supabase_url,
        publishable_key,
    )


def save_feedback(
    rating: int,
    feedback_text: str,
    job_title: str,
    technical_skill_score: float,
) -> tuple[bool, str]:
    if rating < 1 or rating > 5:
        return False, "Please choose a rating between 1 and 5."

    feedback_data = {
        "rating": rating,
        "feedback_text": feedback_text.strip(),
        "job_title": job_title.strip() if job_title else None,
        "technical_skill_score": float(technical_skill_score),
    }

    try:
        supabase = get_supabase_client()

        (
            supabase
            .table("feedback")
            .insert(
                feedback_data,
                returning="minimal",
            )
            .execute()
        )

        return (
            True,
            "Thank you! Your feedback has been submitted successfully.",
        )

    except Exception as error:
        print(f"Feedback submission error: {error}")

        return (
            False,
            "Feedback could not be submitted right now. Please try again later."
        )