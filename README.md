# 🚀 Multi-Agent Research Assistant

A production-ready AI-powered research assistant built using **LangGraph, LangChain, Groq LLM, Tavily Search, Streamlit, Docker, GitHub Actions, and Pytest**.

The application orchestrates multiple AI agents to perform web research, summarize findings, verify information, and generate structured research reports through an automated workflow.

---

## 🌐 Live Demo

https://multi-agent-research-assistant-lamg.onrender.com

---

## ✨ Features

* 🔍 Real-time web research using Tavily Search
* 🤖 Multi-agent workflow powered by LangGraph
* 📝 AI-powered summarization using Groq LLM
* ✅ Information verification agent
* 📄 Professional report generation
* 🎨 Interactive Streamlit interface
* 🧪 Unit testing with Pytest
* ⚙️ Automated CI using GitHub Actions
* 🐳 Dockerized application
* ☁️ Cloud deployment on Render

---

## 🏗️ Architecture

```text
User Query
    │
    ▼
Researcher Agent
    │
    ▼
Summarizer Agent
    │
    ▼
Verifier Agent
    │
    ▼
Report Generator Agent
    │
    ▼
Final Report
```

---

## 🛠️ Tech Stack

### AI & Agents

* LangGraph
* LangChain
* Groq LLM

### Search

* Tavily Search API

### Frontend

* Streamlit

### Testing

* Pytest
* unittest.mock

### CI/CD

* GitHub Actions

### Deployment

* Docker
* Render

### Language

* Python

---

## 📁 Project Structure

```text
multi-agent-research-assistant/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── agents/
│   ├── researcher.py
│   ├── summarizer.py
│   ├── verifier.py
│   └── report_generator.py
│
├── graph/
│   ├── state.py
│   └── workflow.py
│
├── models/
│   └── llm.py
│
├── prompts/
│   ├── report_prompt.py
│   ├── summarizer_prompt.py
│   └── verifier_prompt.py
│
├── tests/
│   ├── test_basic.py
│   ├── test_researcher.py
│   ├── test_summarizer.py
│   ├── test_verifier.py
│   ├── test_report_generator.py
│   └── test_workflow.py
│
├── tools/
│   └── web_search.py
│
├── app.py
├── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd multi-agent-research-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 🧪 Run Tests

Execute the complete test suite:

```bash
python -m pytest -v
```

Run with coverage:

```bash
python -m pytest --cov=. --cov-report=term-missing
```

The project includes unit tests for:

* Graph workflow
* Researcher Agent
* Summarizer Agent
* Verifier Agent
* Report Generator Agent
* End-to-end workflow

External API calls are mocked to ensure fast and reliable testing.

---

## ⚙️ GitHub Actions CI

Every push and pull request automatically:

* Installs project dependencies
* Runs all Pytest test cases
* Builds the Docker image
* Verifies the application is deployment-ready

---

## 🐳 Docker Setup

### Build Image

```bash
docker build -t multi-agent-research .
```

### Run Container

```bash
docker run -p 8501:8501 \
-e GROQ_API_KEY=YOUR_GROQ_KEY \
-e TAVILY_API_KEY=YOUR_TAVILY_KEY \
multi-agent-research
```

---

## ☁️ Deployment

The application is containerized using Docker and deployed on Render.

Deployment workflow:

```text
GitHub
   │
   ▼
GitHub Actions
   │
   ├── Run Pytest
   ├── Build Docker Image
   ▼
Render Deployment
```

---

## 🚀 Future Improvements

* PDF report export
* Research history
* Parallel agent execution
* Citation-based reports
* Resume-to-job matching workflow
* RAG integration
* Multi-language support

---

## 👨‍💻 Author

**Puneeth Kumar**

Aspiring AI Engineer focused on:

* Generative AI
* AI Agents
* LangGraph
* LangChain
* LLM Applications
* AI Product Development

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
