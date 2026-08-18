# ResearchMind - Iterative Web Research Agent

## 1. Problem Statement

ResearchMind is an Agentic AI project that implements a single-agent loop for iterative web research.

The system accepts a research question from the user, uses a real Large Language Model (LLM) to plan the research process, searches the web for relevant information, retrieves a readable webpage, evaluates whether the retrieved information is sufficient, refines the search when necessary, and generates a final cited research summary.

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
- Maximum iteration limit
- Explicit success-condition check
- Iteration logging
- Tool failure recovery
- Iterative query refinement
- Final research summary generation
- Source citation
- Multiple webpage retrieval fallback

---

## 3. Features

- 🤖 Single-agent architecture
- 🧠 LLM-based planning
- 🔎 Web search using DDGS
- 📖 Webpage content extraction
- 🔄 Iterative research loop
- 🔄 Search query refinement
- 🔁 Retry mechanism
- 🛡️ Tool failure recovery
- ✅ Explicit success condition
- 📝 Final research summary
- 🔗 Source URL citation
- 📋 JSON iteration logging
- ⏱️ Maximum iteration limit

---

## 4. Agent Workflow

The ResearchMind agent follows this workflow:

```text
Research Question
       |
       v
   PERCEIVE
       |
       v
     PLAN
  (Ollama LLM)
       |
       v
      ACT
       |
       +----------------------+
       |                      |
       v                      v
  Web Search             Web Reader
     DDGS              Requests + BS4
       |                      |
       +----------+-----------+
                  |
                  v
               OBSERVE
            (Ollama LLM)
                  |
          +-------+-------+
          |               |
       Sufficient       Insufficient
          |               |
          v               v
       Summarize      Refine Query
          |               |
          v               |
      Cited Answer <------+
```

The loop continues until either:

1. The retrieved information is sufficient, or
2. The maximum iteration limit is reached.

---

## 5. Use Case

### UC2 - Iterative Web Research Agent

The agent performs iterative research for a given question.

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
Try Search Results
       |
       v
Retrieve Readable Webpage
       |
       v
Evaluate Information
       |
       +---- Sufficient ----> Generate Summary
       |                           |
       |                           v
       |                      Cite Source
       |
       +---- Insufficient ----> Refine Query
                                    |
                                    v
                              Next Iteration
```

This demonstrates an agent that can perceive information, plan actions, use tools, observe results, refine its approach, and decide whether to continue or finish.

---

## 6. Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| LLM Runtime | Ollama |
| LLM Model | Qwen2.5 3B Instruct |
| Web Search | DDGS |
| Web Reader | Requests + BeautifulSoup4 |
| Logging | JSON |
| Version Control | Git + GitHub |
| Architecture Diagram | Draw.io |

---

## 7. Framework and Software Versions

The following versions are used in the Cycle 1 implementation.

| Component | Version |
|---|---|
| Python | 3.13.5 |
| Ollama | 0.32.6 |
| Qwen2.5 | qwen2.5:3b-instruct |
| DDGS | 9.14.4 |
| Requests | 2.34.2 |
| BeautifulSoup4 | 4.15.0 |

---

## 8. Project Structure

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
│   ├── planner.py
│   └── summarizer.py
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
└── .gitignore
```

---

## 9. Agent Components

### Perceive

Receives the research question from the user.

### Plan

Uses the local Ollama LLM to analyze the question and generate a research plan.

### Act

Uses external tools to:

1. Search the web using DDGS.
2. Try multiple search results.
3. Retrieve webpage content using Requests and BeautifulSoup4.

If one webpage cannot be accessed, the agent attempts another search result.

### Observe

Uses the LLM to determine whether the retrieved webpage contains enough relevant information.

If the information is insufficient, the observer produces a refined search query.

### Summarize

When sufficient information has been collected, the summarizer generates a concise answer using the retrieved webpage and includes the source URL.

---

## 10. Tool Failure Recovery

ResearchMind is designed to continue operating when a tool fails.

### Webpage Reader Failure

If a webpage cannot be retrieved:

```text
Reader failed: 403 Client Error: Forbidden
⚠️ Could not read this result. Trying the next result...
```

The system attempts the next available search result.

If all results fail:

```text
❌ Could not retrieve any webpage from the search results.
```

The failure is passed to the observation stage and the agent continues to the next iteration instead of crashing.

### Demonstrated Recovery

A controlled reader failure was intentionally demonstrated during Cycle 1 testing.

The agent produced:

```text
Reader failed: DEMO FAILURE - Simulated webpage reader failure
```

and continued through subsequent iterations without crashing.

The temporary failure was then removed and the original reader implementation was restored.

---

## 11. Iteration Logging

Every agent iteration is logged to:

```text
logs/agent_log.json
```

The log records:

- Iteration number
- Research question
- LLM thought
- Plan
- Retrieved action content
- Source URL
- Observation
- Success status

Example:

```json
{
    "iteration": 1,
    "question": "What is Agentic AI?",
    "thought": "...",
    "plan": "...",
    "action": "...",
    "source_url": "https://example.com",
    "observation": "Information was sufficient",
    "success": true
}
```

The iteration trace can be manually reviewed to verify the agent's behavior.

---

## 12. Maximum Iterations

The agent uses a maximum iteration limit to prevent infinite execution.

The current implementation uses:

```python
max_iterations = 3
```

The agent stops when either:

1. The research information is sufficient, or
2. The maximum number of iterations is reached.

---

## 13. Local LLM Setup

ResearchMind uses **Ollama** to run the LLM locally.

Verify the installation:

```powershell
ollama --version
```

Verify the model:

```powershell
ollama list
```

The required model is:

```text
qwen2.5:3b-instruct
```

If the model has not been downloaded:

```powershell
ollama pull qwen2.5:3b-instruct
```

Test the model:

```powershell
ollama run qwen2.5:3b-instruct
```

Exit the interactive session with:

```text
/bye
```

---

## 14. Requirements

The project dependencies are specified in:

```text
requirements.txt
```

The main dependencies are:

```text
ddgs==9.14.4
requests==2.34.2
beautifulsoup4==4.15.0
```

Ollama is installed separately as a local application and is not installed through `pip`.

---

## 15. Installation

### Step 1 - Clone the repository

```powershell
git clone <your-github-repository-url>
cd agentic-ai-preparation
```

### Step 2 - Create a virtual environment

```powershell
python -m venv .venv
```

### Step 3 - Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

### Step 4 - Install Python dependencies

```powershell
pip install -r requirements.txt
```

### Step 5 - Verify Ollama

```powershell
ollama --version
```

### Step 6 - Verify the model

```powershell
ollama list
```

If required:

```powershell
ollama pull qwen2.5:3b-instruct
```

---

## 16. Running the Project

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

Make sure Ollama is available and the required model is installed:

```powershell
ollama list
```

Run the agent:

```powershell
python main.py
```

The program will ask for a research question.

---

## 17. Sample Input

```text
what is agentic AI?
```

---

## 18. Sample Output

A successful execution follows this general flow:

```text
==================================================
🤖 Welcome to ResearchMind
==================================================

🔍 Enter your research question: what is agentic AI?

========== Iteration 1 ==========

🧠 Thought: ...
📌 Plan: ...

🛠️ Searching for information...
✅ Found 5 search results

📖 Trying search results...

🔗 Trying result 1: ...
⚠️ Could not read this result. Trying the next result...

🔗 Trying result 2: ...
✅ Retrieved webpage content

📋 Checking if enough information was found...
✅ Information is sufficient

✅ Research Completed!

📝 Generating final research summary...

==================================================
📝 FINAL RESEARCH ANSWER
==================================================

Answer:
...

Source:
https://...

🏁 Agent Finished
```

The exact LLM-generated thought, plan, and answer may vary between executions.

---

## 19. Final Research Summary

When sufficient information is found, ResearchMind generates a final answer based on the retrieved webpage.

The output contains:

```text
Answer:
<research summary>

Source:
<source URL>
```

The summary is generated using the retrieved webpage content and the original research question.

---

## 20. Git Workflow

The project is maintained using incremental Git commits.

Each development stage is committed separately to maintain a clear development history.

Example:

```powershell
git add .
git commit -m "Week 1 Day 11 - Finalize Cycle 1 documentation"
git push
```

---

## 21. Security

ResearchMind does not require an external API key for the Cycle 1 LLM implementation because Ollama runs locally.

Security practices include:

- No API keys are stored in source code.
- No secrets are committed to GitHub.
- `.env` is not required for the current Ollama implementation.
- Local configuration and generated files should be reviewed before committing.

---

## 22. Architecture Diagram

The Cycle 1 architecture diagram is available in:

```text
docs/architecture.drawio
docs/architecture.png
```

The diagram represents the Perceive → Plan → Act → Observe agent loop, including the LLM, web search, webpage reader, iteration control, logging, and final summary generation.

---

## 23. Testing and Verification

Cycle 1 was manually tested using real research questions.

Testing verified:

- Successful LLM planning
- Web search execution
- Webpage retrieval
- Multiple-result fallback
- LLM-based information evaluation
- Search query refinement
- Maximum iteration handling
- Tool failure recovery
- JSON iteration logging
- Final answer generation
- Source URL citation

A successful final execution was verified with:

```text
Search → Webpage Retrieval → Observation → Success → Summary → Source
```

A controlled webpage-reader failure was also demonstrated without crashing the agent.

---

## 24. Future Improvements

Potential future improvements include:

- Improved webpage ranking
- Multiple-source research
- More advanced evidence evaluation
- Better citation formatting
- Improved query refinement
- Additional research tools
- MCP-based tool integration

These improvements are outside the current Cycle 1 implementation.

---

## 25. Author

**S. P. Abishek Edwin Raj**

B.Tech - Artificial Intelligence and Data Science

J.J. College of Engineering and Technology