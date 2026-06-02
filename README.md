# 🚀 Multi-Agent Research Assistant

A powerful AI-powered research assistant built using LangGraph, Groq LLM, Tavily Search, Streamlit, and Docker.

The application uses multiple AI agents working together to perform web research, summarize findings, verify information, and generate professional reports.

## 🌐 Live Demo

https://multi-agent-research-assistant-lamg.onrender.com

## 📂 GitHub Repository

Add your GitHub repository link here.

---

## ✨ Features

* 🔍 Real-time web research using Tavily Search
* 🤖 Multi-agent workflow using LangGraph
* 📝 AI-powered summarization
* ✅ Information verification agent
* 📄 Professional report generation
* 🎨 Interactive Streamlit UI
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
├── app.py
├── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
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
│   ├── researcher_prompt.py
│   ├── summarizer_prompt.py
│   ├── verifier_prompt.py
│   └── report_prompt.py
│
└── tools/
    └── web_search.py
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

Windows:

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

## 🐳 Docker Setup

### Build Image

```bash
docker build -t multi-agent-research .
```

### Run Container

```bash
docker run -p 8501:8501 -e GROQ_API_KEY=YOUR_GROQ_KEY -e TAVILY_API_KEY=YOUR_TAVILY_KEY multi-agent-research
```

---

## ☁️ Deployment

The application is containerized using Docker and deployed on Render.

Deployment workflow:

```text
GitHub
   │
   ▼
Render
   │
   ▼
Docker Build
   │
   ▼
Live Application
```

---

## 📸 Screenshots

Add screenshots of:

1. Home Page
2. Research Query
3. Generated Report
4. Docker Deployment

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

Puneeth Kumar

Aspiring AI Engineer focused on:

* Generative AI
* AI Agents
* LangGraph
* LangChain
* LLM Applications
* AI Product Development

---

## ⭐ If you found this project useful, please give it a star!
