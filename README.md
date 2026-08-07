# ResearchMind - Iterative Web Research Agent

## Problem Statement

ResearchMind is an Agentic AI project that answers research questions using an iterative agent loop. The agent searches the web, reads the top webpage, evaluates whether enough information has been gathered, and either stops or retries until a maximum iteration limit is reached.

This project implements **Use Case 2 (Iterative Web Research Agent)** from the AI Development Preparation assignment.

---

## Features

- Perceive → Plan → Act → Observe agent loop
- Real LLM integration using OpenRouter
- Web search tool
- Webpage reader tool
- Iteration logging in JSON format
- Maximum iteration limit
- Explicit success condition
- Tool failure recovery

---

## Project Structure

```
agent/
    actions.py
    llm.py
    logger.py
    observer.py
    perceive.py
    planner.py

config/
    settings.py

tools/
    search.py
    reader.py

logs/
main.py
requirements.txt
README.md
```

---

## Technology Stack

| Component | Technology |
|----------|------------|
| Language | Python 3.13 |
| LLM | OpenRouter API |
| Search | DDGS |
| Web Reader | Requests + BeautifulSoup4 |
| Logging | JSON |
| Environment | python-dotenv |

---

## SDK / Framework Versions

| Package | Version |
|----------|----------|
| openai | 2.51.0 |
| ddgs | Installed via pip |
| requests | 2.34.2 |
| beautifulsoup4 | Latest |
| python-dotenv | 1.2.2 |

---

## Installation

Create a virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file

```
OPENROUTER_API_KEY=your_api_key
```

---

## Run

```bash
python main.py
```

---

## Sample Input

```
What is Agentic AI?
```

---

## Sample Output

```
Planning...

Searching...

Reading webpage...

Research Completed!

Agent Finished
```

---

## Future Improvements

- Citation generation
- Better webpage ranking
- Multiple webpage summarization
- Automatic query refinement

---

## Author

S. P. Abishek Edwin Raj

B.Tech Artificial Intelligence and Data Science

J.J. College of Engineering and Technology