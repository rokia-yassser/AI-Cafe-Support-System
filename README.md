# ☕ AI Cafe Support System

An AI-powered multi-agent customer support system for cafes and restaurants built with:

- FastAPI
- Streamlit
- LangGraph
- OpenRouter LLMs
- FAISS Vector Database
- SQLite
- RAG (Retrieval-Augmented Generation)

The system can:
- Answer customer questions
- Search cafe knowledge base PDFs
- Detect customer sentiment
- Handle escalation decisions
- Store conversations in SQLite
- Support order-based interactions

---

# 🚀 Features

##  Multi-Agent Architecture

The system uses multiple AI agents:

| Agent | Responsibility |
|---|---|
| Conversation Manager | Generates final customer response |
| Knowledge Agent | Retrieves information from RAG |
| Sentiment Agent | Detects customer mood |
| Action Agent | Detects customer intent/actions |
| Escalation Agent | Determines if human help is needed |
| Learning Agent | Stores conversation learning data |

---

#  RAG Knowledge Base

The system uses PDF documents as a knowledge base.

Examples:
- menu.pdf
- refund_policy.pdf
- cafe_hours.pdf
- faq.pdf

Documents are:
1. Loaded
2. Split into chunks
3. Embedded
4. Stored in FAISS vector database

---

# 🏗 Project Structure

```text
ai-cafe-support/
│
├── app/
│   │
│   ├── agents/
│   │   ├── action_agent.py
│   │   ├── conversation_manager.py
│   │   ├── escalation_agent.py
│   │   ├── graph.py
│   │   ├── knowledge_agent.py
│   │   ├── learning_agent.py
│   │   └── sentiment_agent.py
│   │
│   ├── api/
│   │   ├── main.py
│   │   └── routes/
│   │       └── chat.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── llm.py
│   │   └── prompts.py
│   │
│   ├── db/
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── ingest.py
│   │   ├── models.py
│   │   └── vector_store.py
│   │
│   └── models/
│       ├── request_models.py
│       ├── response_models.py
│       └── state.py
│
├── streamlit_app/
│   └── app.py
│
├── vector_store/
│
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <https://github.com/rokia-yassser/AI-Cafe-Support-Systemyour_repo_url>
cd ai-cafe-support
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create `.env` 


# IMPORTANT: Build Vector Database First

Before running the server, you MUST run:

```bash
python app/db/ingest.py
```

This creates:

```text
vector_store/
│
├── index.faiss
└── index.pkl
```

Without this step the RAG system will not work.

---

# ▶️ Run FastAPI Server

```bash
uvicorn app.api.main:app --reload
```

Server runs on:

```text
http://127.0.0.1:8000
```

Swagger docs:

```text
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Streamlit UI

Open another terminal:

```bash
streamlit run streamlit_app/app.py
```

---

# 🗄 SQLite Database

The system automatically creates:

```text
cafe_support.db
```

Stored data:
- order_id
- customer message
- conversation summary
- sentiment
- escalation status
- AI final response

---

# 🧪 Example Questions

Try asking:

- "How much is espresso?"
- "Do you have vegan options?"
- "I want a refund"
- "Where is my order?"
- "What desserts do you have?"
- "Can I reserve a table?"

---

# 🔥 Tech Stack

| Technology | Purpose |
|---|---|
| FastAPI | Backend API |
| Streamlit | Frontend UI |
| LangGraph | Multi-agent orchestration |
| OpenRouter | LLM Provider |
| FAISS | Vector database |
| SQLite | Persistent storage |
| LangChain | RAG + LLM tooling |

---

# 📌 Future Improvements

Possible future upgrades:

- Admin dashboard
- Human live chat takeover
- PostgreSQL
- Redis memory
- WhatsApp integration
- Slack notifications
- Order tracking APIs
- Voice assistant
- Multi-language support

