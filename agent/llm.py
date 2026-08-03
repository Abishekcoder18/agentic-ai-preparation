import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def ask_llm(prompt):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "openai/gpt-oss-20b:free",
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data,
    )

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]