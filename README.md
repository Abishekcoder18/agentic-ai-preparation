# ResearchMind - Iterative Web Research Agent

## 1. Problem Statement

ResearchMind is an Agentic AI project that implements a single-agent loop for iterative web research.

The system accepts a research question from the user, uses a real Large Language Model (LLM) to plan the research process, searches the web for relevant information, reads a webpage, observes the result, and decides whether the research is complete or another iteration is required.

This project implements **Use Case 2 - Iterative Web Research Agent** from the AI Development Preparation assignment.

The agent follows the:

**Perceive → Plan → Act → Observe**

loop with a maximum iteration limit, an explicit success condition, iteration logging, and tool failure recovery.

---

## 2. Cycle 1 Requirements Implemented

The following Agent Loop requirements are implemented:

- Single-agent Perceive → Plan → Act → Observe loop
- Real LLM call during the Plan stage
- Web search tool
- Webpage reader tool
- Maximum iteration count
- Explicit success-condition check
- Iteration logging
- Tool failure recovery
- Iterative web research workflow

---

## 3. Features

- 🤖 Single-agent architecture
- 🧠 LLM-based planning
- 🔍 Web search using DDGS
- 📖 Webpage content extraction
- 🔄 Iterative retry mechanism
- ✅ Explicit success condition
- 📝 JSON iteration logging
- 🛡️ Tool failure recovery
- 🔐 API key protection using environment variables

---

## 4. Architecture

The system follows a modular agent architecture based on the Perceive → Plan → Act → Observe cycle.

The complete one-page architecture diagram is available here:

**`docs/architecture.png`**

The editable Draw.io source is available here:

**`docs/architecture.drawio`**

---

## 5. Agent Loop

### Perceive

The agent receives a research question from the user.

Example:

```text
What is Agentic AI?
```

### Plan

The planner sends the question to a real LLM through the OpenRouter API.

The LLM generates:

- A research thought
- A research plan

### Act

The agent performs actions using callable tools:

1. Web search
2. Webpage reading

### Observe

The agent checks whether enough information was obtained.

If successful:

```text
Research Completed!
```

If unsuccessful, the agent continues to the next iteration until the maximum iteration count is reached.

---

## 6. Tools

### Web Search Tool

File:

```text
tools/search.py
```

Function:

```python
search_web(query)
```

The tool searches the web using DDGS and returns search results.

### Webpage Reader Tool

File:

```text
tools/reader.py
```

Function:

```python
fetch_webpage(url)
```

The tool retrieves a webpage and extracts readable text using Requests and BeautifulSoup4.

---

## 7. Tool Failure Recovery

The agent is designed to recover from tool failures without crashing.

### Search Failure

If the search tool fails:

```text
⚠️ Search failed. Will retry in the next iteration.
```

The agent returns control to the loop and attempts another iteration.

### Webpage Reader Failure

If the webpage cannot be retrieved:

```text
⚠️ Failed to read webpage. Will retry in the next iteration.
```

The agent continues according to the iteration limit.

---

## 8. Iteration Logging

Every agent iteration is logged to:

```text
logs/agent_log.json
```

The log records information such as:

- Iteration number
- User question
- LLM thought
- Plan
- Action
- Observation
- Success status

Example:

```json
{
    "iteration": 1,
    "question": "What is Agentic AI?",
    "thought": "...",
    "plan": "...",
    "action": "Search executed",
    "observation": "Information was retrieved",
    "success": true
}
```

The iteration trace can be manually reviewed to verify the agent's behavior.

---

## 9. Project Structure

```text
agentic-ai-preparation/
│
├── agent/
│   ├── __init__.py
│   ├── actions.py
│   ├── llm.py
│   ├── logger.py
│   ├── observer.py
│   ├── perceive.py
│   └── planner.py
│
├── config/
│   └── settings.py
│
├── tools/
│   ├── search.py
│   └── reader.py
│
├── docs/
│   ├── architecture.drawio
│   └── architecture.png
│
├── logs/
│   └── agent_log.json
│
├── tests/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

> `.env` contains local secrets and is excluded from Git using `.gitignore`.

---

## 10. Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| LLM API | OpenRouter |
| LLM SDK | OpenAI Python SDK |
| Web Search | DDGS |
| Web Reader | Requests + BeautifulSoup4 |
| Logging | JSON |
| Configuration | python-dotenv |
| Version Control | Git + GitHub |
| Architecture Diagram | Draw.io |

---

## 11. Framework and SDK Versions

The following versions are used in the Cycle 1 implementation.

| Component | Version |
|---|---|
| Python | 3.13.5 |
| OpenAI Python SDK | 2.51.0 |
| DDGS | 9.14.4 |
| Requests | 2.34.2 |
| BeautifulSoup4 | 4.15.0 |
| python-dotenv | 1.2.2 |

---

## 12. Requirements

The project dependencies are specified in:

```text
requirements.txt
```

Important direct dependencies include:

```text
ddgs==9.14.4
requests==2.34.2
beautifulsoup4==4.15.0
openai==2.51.0
python-dotenv==1.2.2
```

---

## 13. Installation

### Step 1 - Clone the repository

```bash
git clone <your-github-repository-url>
cd agentic-ai-preparation
```

### Step 2 - Create a virtual environment

```bash
python -m venv .venv
```

### Step 3 - Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 4 - Install dependencies

```powershell
pip install -r requirements.txt
```

---

## 14. Environment Variables

Create a local `.env` file in the project root:

```text
OPENROUTER_API_KEY=your_api_key_here
```

The API key must not be committed to GitHub.

The `.env` file is included in `.gitignore`.

---

## 15. Running the Project

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

Run the agent:

```powershell
python main.py
```

The program will ask for a research question.

---

## 16. Sample Input

```text
What is Agentic AI?
```

---

## 17. Sample Output

A successful execution follows this general flow:

```text
==================================================
🤖 Welcome to ResearchMind
==================================================

🔍 Enter your research question: What is Agentic AI?

========== Iteration 1 ==========

🧠 Thought: ...
📌 Plan: ...

🛠️ Searching for information...
✅ Found 5 search results

📖 Reading the top result...
✅ Retrieved webpage content

📋 Checking if enough information was found...

✅ Research Completed!

🏁 Agent Finished
```

The exact LLM-generated thought and plan may vary between executions.

---

## 18. Failure Recovery Example

If a tool fails, the agent does not immediately terminate.

Example:

```text
🛠️ Searching for information...

⚠️ Search failed. Will retry in the next iteration.

========== Iteration 2 ==========
```

The loop continues until the research succeeds or the maximum iteration count is reached.

---

## 19. Maximum Iterations

The agent uses a maximum iteration limit to prevent an infinite loop.

The current implementation uses:

```python
max_iterations = 3
```

The agent stops when either:

1. The success condition is reached, or
2. The maximum number of iterations is reached.

---

## 20. Git Workflow

The project is maintained using incremental Git commits.

Each development stage is committed separately to maintain a clear development history.

Example:

```bash
git add .
git commit -m "Week 1 Day 10 - Document exact project versions and dependencies"
git push
```

---

## 21. Use Case

### UC2 - Iterative Web Research Agent

The agent is designed to perform iterative research for a given question.

The workflow is:

```text
Research Question
       |
       v
Generate Plan
       |
       v
Search Web
       |
       v
Read Top Result
       |
       v
Observe Result
       |
       +---- Success ----> Finish
       |
       +---- Failure ----> Retry
```

This demonstrates an agent that can repeatedly perceive information, plan actions, use tools, observe results, and decide whether to continue.

---

## 22. Security

- API keys are stored in `.env`.
- `.env` is excluded through `.gitignore`.
- Secrets are not included in the source code.
- API keys must never be committed to GitHub.

---

## 23. Future Improvements

Potential future improvements include:

- Improved webpage ranking
- Query refinement
- Citation generation
- Multiple-source research
- More advanced result evaluation

These improvements are outside the current Cycle 1 implementation.

---

## 24. Author

**S. P. Abishek Edwin Raj**

B.Tech - Artificial Intelligence and Data Science

J.J. College of Engineering and Technology