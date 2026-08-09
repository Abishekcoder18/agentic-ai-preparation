import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:3b-instruct"


def ask_llm(prompt):
    """
    Send a prompt to the local Ollama model.

    Args:
        prompt (str): Prompt sent to the LLM.

    Returns:
        str: Generated response.
    """

    data = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=data,
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"]