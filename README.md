# 🔍 Deep Research Agent

An AI-powered multi-agent research assistant that generates comprehensive, well-structured research reports on any topic. The system automatically plans the research process, retrieves relevant information from the web, and synthesizes the findings into a coherent report through a Planner–Researcher–Analyst workflow.

### ✨ Key Features

* 🧠 Multi-agent architecture using LangGraph
* 📋 Automated research planning
* 🌐 Web search integration with Tavily
* 🤖 Google Gemini for reasoning and report generation
* 📄 Structured research reports
* 🎨 Interactive Streamlit web interface
* 📥 Download generated reports as Markdown

## 🏗️ Architecture

The application follows a **multi-agent workflow** built with LangGraph. Each agent has a single responsibility, making the system modular, maintainable, and easy to extend.

### Workflow

```text
                    User
                      │
                      ▼
             Streamlit Interface
                      │
                      ▼
              LangGraph Workflow
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   Planner Agent  Research Agent  Analyst Agent
        │             │             │
        │      Tavily Search API    │
        └─────────────┼─────────────┘
                      ▼
              Google Gemini LLM
                      │
                      ▼
        Final Research Report
```

### Agent Responsibilities

* **Planner Agent** – Breaks the user's query into a structured research plan.
* **Research Agent** – Searches the web for each research section using Tavily Search.
* **Analyst Agent** – Synthesizes the collected information into a comprehensive research report and analysis.

## 🛠️ Tech Stack

| Category                   | Technologies            |
| -------------------------- | ----------------------- |
| **Programming Language**   | Python                  |
| **LLM**                    | Google Gemini 2.5 Flash |
| **AI Framework**           | LangChain               |
| **Agent Orchestration**    | LangGraph               |
| **Web Search**             | Tavily Search API       |
| **Frontend**               | Streamlit               |
| **Data Validation**        | Pydantic                |
| **Environment Management** | python-dotenv           |
| **Version Control**        | Git & GitHub            |

## 📂 Project Structure

```text
deep-research-agent/
│
├── core/
│   └── config.py
│
├── graph/
│   ├── nodes.py
│   ├── state.py
│   └── workflow.py
│
├── llm/
│   └── gemini.py
│
├── prompts/
│   ├── planner_prompt.py
│   └── analysis_prompt.py
│
├── schemas/
│   ├── planner_output.py
│   └── analysis_output.py
│
├── app.py
├── main.py
├── search.py
├── requirements.txt
├── README.md
└── .env.example
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/adithya-ram000/deep-research-agent.git
cd deep-research-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 5. Launch the application

```bash
streamlit run app.py
```

## 🚀 Usage

1. Launch the Streamlit application.
2. Enter any research topic.
3. Click **🚀 Generate Report**.
4. The Planner Agent creates a research plan.
5. The Research Agent gathers relevant information from the web.
6. The Analyst Agent generates a comprehensive research report.
7. View the report, analysis, and research plan in separate tabs.
8. Download the generated report as a Markdown file.
