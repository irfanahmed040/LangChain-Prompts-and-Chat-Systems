# LangChain Prompt Engineering and Chat Systems

This repository implements structured prompt engineering workflows using LangChain, covering chat message orchestration, template serialization, memory injection, and UI-driven parameterized generation.

The project focuses on building reusable, production-oriented prompt pipelines rather than ad-hoc prompt experimentation.

---

## Architecture Overview

The repository demonstrates:

- Structured `PromptTemplate` design
- `ChatPromptTemplate` with role-based message control
- Explicit conversation state management
- `MessagesPlaceholder` for dynamic memory injection
- Prompt serialization and loading via JSON
- Parameterized generation through a Streamlit interface

The goal is to design modular prompt systems that can scale into larger AI workflows such as RAG, agents, or tool-driven pipelines.

---

## Repository Structure

```
LANGCHAIN PROMPTS/
│
├── chat_prompt_template.py      # Role-based chat template construction
├── chatbot.py                   # Stateful multi-turn chat loop
├── messages.py                  # Explicit message handling with ChatOpenAI
├── message_placeholder.py       # Chat history injection via MessagesPlaceholder
├── prompt_generator.py          # Structured PromptTemplate creation + serialization
├── prompt_ui.py                 # Streamlit-based parameterized generation UI
├── template.json                # Serialized prompt definition
├── chat_history.txt             # External conversation history
├── requirements.txt
└── .env
```

---

## Core Components

### PromptTemplate Serialization

- Defines a structured research summarization template
- Parameterized by:
  - Paper title
  - Explanation style
  - Explanation length
- Saved to `template.json` for reuse across applications

This enforces separation between:
- Prompt definition
- Runtime variable injection
- Model execution

---

### ChatPromptTemplate and Role Control

Implements structured chat roles:

- `system`
- `human`
- `ai`

Demonstrates deterministic prompt construction through explicit role specification.

---

### Conversation State Management

Implements manual memory handling:

- Appends `SystemMessage`, `HumanMessage`, and `AIMessage`
- Maintains multi-turn conversation history
- Demonstrates deterministic message sequencing

---

### Memory Injection via MessagesPlaceholder

- Loads historical conversation from file
- Injects it dynamically into the prompt
- Separates memory storage from prompt logic

This pattern is foundational for scalable chat systems.

---

### Parameterized Generation UI

`prompt_ui.py` integrates:

- Template loading from JSON
- Runtime parameter injection
- Controlled summarization generation
- Streamlit UI for interactive execution

This demonstrates bridging:
Prompt layer → Model layer → Interface layer

---

## Tech Stack

- Python
- LangChain
- langchain-openai
- Streamlit
- python-dotenv
- NumPy
- scikit-learn

---

## Installation

```bash
git clone https://github.com/irfanahmed040/LangChain-Prompts-and-Chat-Systems.git
cd LangChain-Prompts-and-Chat-Systems
```

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key_here
```

Ensure `.env` is excluded via `.gitignore`.

---

## Execution

Run CLI chatbot:

```bash
python chatbot.py
```

Run prompt template demo:

```bash
python chat_prompt_template.py
```

Run memory injection demo:

```bash
python message_placeholder.py
```

Run Streamlit interface:

```bash
streamlit run prompt_ui.py
```

---

## Engineering Focus

This repository emphasizes:

- Deterministic prompt construction
- Separation of concerns (template vs execution)
- Reusable prompt definitions
- Structured conversation state handling
- Scalable prompt architecture

It serves as a foundational layer for:

- Retrieval-Augmented Generation (RAG)
- Agent frameworks
- Tool-calling pipelines
- Production AI systems
