from pathlib import Path
import os

from dotenv import load_dotenv
from groq import Groq, RateLimitError


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

MODEL_NAME = "llama-3.3-70b-versatile"


def ask_groq(prompt: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY was not found. "
            "Check your local .env file or Streamlit Cloud secrets."
        )

    client = Groq(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.1,
        )

        content = response.choices[0].message.content

        if not content:
            raise ValueError(
                "The AI service returned an empty response."
            )

        return content

    except RateLimitError as error:
        raise RuntimeError(
            "Daily AI usage limit reached. "
            "Please try again later."
        ) from error