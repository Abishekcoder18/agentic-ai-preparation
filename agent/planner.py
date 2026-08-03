from agent.llm import ask_llm


def plan(question):

    prompt = f"""
You are an AI Research Agent.

The user asked:

{question}

Think step by step.

Return your answer in exactly this format:

Thought:
<your thought>

Plan:
<your plan>
"""

    response = ask_llm(prompt)

    thought = ""
    plan = ""

    if "Plan:" in response:

        parts = response.split("Plan:")

        thought = parts[0].replace("Thought:", "").strip()

        plan = parts[1].strip()

    else:

        thought = response

        plan = "Search the web."

    print(f"🧠 Thought: {thought}")
    print(f"📌 Plan: {plan}")

    return thought, plan