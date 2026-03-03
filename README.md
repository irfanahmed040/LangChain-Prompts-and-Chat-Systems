# LangChain Prompt Engineering and Chat Systems

This repository implements structured prompt engineering workflows using LangChain.  
It explores prompt templating, role-based chat construction, conversation memory injection, template serialization, and UI-driven parameterized generation.

The goal is to design modular, reusable prompt systems that can scale into larger AI architectures such as RAG pipelines, agents, and production AI services.

---

# Architecture Philosophy

This repository is structured around three core principles:

1. Separation of prompt definition from execution  
2. Explicit control over conversation state  
3. Reusability through template serialization  

Rather than writing inline prompts inside model calls, this project isolates prompt logic into composable components.

---

# Repository Structure

```
LANGCHAIN PROMPTS/
│
├── chat_prompt_template.py
├── chatbot.py
├── messages.py
├── message_placeholder.py
├── prompt_generator.py
├── prompt_ui.py
├── template.json
├── chat_history.txt
├── requirements.txt
└── .env
```

---

# File-by-File Explanation

## 1. chat_prompt_template.py

Purpose:
Demonstrates structured role-based chat prompt construction using `ChatPromptTemplate`.

What it does:
- Defines a system message with a dynamic `{domain}` variable
- Defines a human message with a `{topic}` variable
- Injects runtime variables into the template
- Produces a structured chat prompt object

Why this matters:
This establishes deterministic prompt construction instead of string concatenation, enabling structured, reusable prompt workflows.

---

## 2. chatbot.py

Purpose:
Implements a stateful, multi-turn CLI chatbot using `ChatOpenAI`.

What it does:
- Initializes a system message
- Accepts user input in a loop
- Appends `HumanMessage` to conversation history
- Invokes the model with full message history
- Appends `AIMessage` back into memory
- Maintains conversational continuity

Why this matters:
Demonstrates explicit conversation state management — foundational for production chat systems and memory-driven agents.

---

## 3. messages.py

Purpose:
Demonstrates structured message passing to a chat model.

What it does:
- Creates `SystemMessage` and `HumanMessage`
- Invokes the model with structured messages
- Appends the AI response back into the message list

Why this matters:
Shows how LangChain handles role-specific message objects rather than raw text prompts.

---

## 4. message_placeholder.py

Purpose:
Demonstrates dynamic chat history injection using `MessagesPlaceholder`.

What it does:
- Defines a `ChatPromptTemplate` with a memory placeholder
- Loads historical conversation from `chat_history.txt`
- Injects history into the prompt dynamically
- Executes a new query with prior context

Why this matters:
Separates memory storage from prompt structure.  
This pattern is foundational for scalable memory-enabled systems.

---

## 5. chat_history.txt

Purpose:
External storage of prior conversation history.

Why this matters:
Decouples memory from runtime execution, allowing persistence, retrieval, and future integration with vector databases.

---

## 6. prompt_generator.py

Purpose:
Defines a structured research summarization prompt using `PromptTemplate` and serializes it to disk.

What it does:
- Creates a parameterized summarization template
- Defines required variables:
  - `paper_input`
  - `style_input`
  - `length_input`
- Saves the template to `template.json`

Why this matters:
Separates prompt definition from application logic and enables reuse across different execution environments.

---

## 7. template.json

Purpose:
Serialized representation of the research summarization prompt.

Why this matters:
- Enables loading prompts dynamically
- Promotes reuse
- Supports scalable architecture
- Allows centralized prompt management

---

## 8. prompt_ui.py

Purpose:
Implements a Streamlit-based interface for parameterized prompt execution.

What it does:
- Loads `template.json`
- Injects runtime parameters selected from UI
- Invokes OpenAI model
- Displays structured output

Why this matters:
Demonstrates integration of:
Prompt layer → Model layer → Interface layer

This is a minimal prototype of a controllable AI application.

---

## 9. requirements.txt

Lists all required dependencies including:

- LangChain
- langchain-openai
- Streamlit
- HuggingFace integrations
- Anthropic integration
- Google Generative AI integration
- NumPy
- scikit-learn
- python-dotenv

The repository is structured to allow multi-provider model integration.

---

# Core Concepts Demonstrated

- PromptTemplate
- ChatPromptTemplate
- Role-based message control
- Manual conversation state management
- MessagesPlaceholder
- Prompt serialization (JSON)
- Parameterized prompt execution
- Model abstraction via LangChain
- Interface-layer integration

---

# Installation

Clone the repository:

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

# Environment Configuration

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key_here
```

Ensure `.env` is added to `.gitignore`.

---

# Running the Modules

CLI chatbot:

```bash
python chatbot.py
```

Chat template demo:

```bash
python chat_prompt_template.py
```

Memory injection demo:

```bash
python message_placeholder.py
```

Streamlit interface:

```bash
streamlit run prompt_ui.py
```

---

# Engineering Focus

This repository emphasizes:

- Deterministic prompt construction
- Separation of concerns
- Reusable prompt definitions
- Explicit memory handling
- Structured AI application design

It serves as a foundational layer for:

- Retrieval-Augmented Generation (RAG)
- Agent frameworks
- Tool-using models
- Production AI systems
