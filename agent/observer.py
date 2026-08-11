from agent.llm import ask_llm


def observe(question, page_content):
    print("📋 Checking if enough information was found...")

    if not page_content:
        print("⚠️ No webpage content available.")
        return False, ""

    prompt = f"""
You are the evaluation step of a web research agent.

Research question:
{question}

Retrieved webpage:
{page_content[:6000]}

Decide whether this webpage contains enough useful information
to answer the research question.

For a simple definition question such as:
"What is agentic AI?"

A webpage is sufficient if it explains the concept, definition,
characteristics, meaning, or examples of agentic AI.

Do not reject a webpage just because it does not contain every
possible detail.

IMPORTANT:
"agentic AI" means AI systems capable of autonomous or goal-directed
actions. Do not interpret "agentic" as "agenetic", "genetic",
genetic algorithms, or evolutionary AI.

Return exactly:

Sufficient: YES or NO
Reason: <one short sentence>
Refined Query: <better search query or NONE>
"""

    response = ask_llm(prompt).strip()

    sufficient = False
    reason = ""
    refined_query = question

    for line in response.splitlines():
        line = line.strip()

        if line.lower().startswith("sufficient:"):
            value = line.split(":", 1)[1].strip().upper()
            sufficient = value == "YES"

        elif line.lower().startswith("reason:"):
            reason = line.split(":", 1)[1].strip()

        elif line.lower().startswith("refined query:"):
            refined_query = line.split(":", 1)[1].strip()

    if sufficient:
        print("✅ Information is sufficient")
        return True, "Information was sufficient"

    if refined_query.upper() == "NONE" or not refined_query:
        refined_query = question

    print("❌ Information is insufficient")
    print(f"🔄 Refined query: {refined_query}")

    return False, refined_query