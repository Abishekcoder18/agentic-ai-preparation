from agent.llm import ask_llm


def generate_summary(question, page_content, source_url):
    print("\n📝 Generating final research summary...")

    prompt = f"""
You are a research assistant.

Research question:
{question}

Retrieved source content:
{page_content[:8000]}

Answer the research question using only the information supported
by the retrieved source.

Write a concise, factual summary.

Do not invent information.

Return exactly this format:

Answer:
<your answer>

Source:
{source_url}
"""

    response = ask_llm(prompt)

    return response