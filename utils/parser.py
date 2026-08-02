import json


def parse_json_response(ai_response: str) -> dict:
    if not ai_response or not ai_response.strip():
        raise ValueError("The AI returned an empty response.")

    cleaned_response = ai_response.strip()

    if cleaned_response.startswith("```json"):
        cleaned_response = cleaned_response[7:]
    elif cleaned_response.startswith("```"):
        cleaned_response = cleaned_response[3:]

    if cleaned_response.endswith("```"):
        cleaned_response = cleaned_response[:-3]

    cleaned_response = cleaned_response.strip()

    try:
        return json.loads(cleaned_response)

    except json.JSONDecodeError as error:
        raise ValueError(
            "The AI response was not valid JSON."
        ) from error