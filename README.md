NyayaConsult – Law System Project ⚖️

> An AI-powered legal consultation and research assistant using Retrieval-Augmented Generation (RAG), structured conversation memory, and a scalable backend architecture.

---

## 🚧 Project Status: **Active Development (Foundation Completed)**

NyayaConsult has progressed beyond experimentation and is now in **core backend and data pipeline development**.
The database, migration system, and foundational architecture are fully implemented.

---

## 🎯 Project Objective

NyayaConsult aims to:

* Answer legal queries using **context-aware AI**
* Retrieve information from **Indian legal documents**
* Maintain **persistent conversation memory**
* Summarize long legal discussions
* Classify queries by **law domain**
* Provide a scalable foundation for future legal tooling

---

## 📁 Repository Structure

```
.
├── backend/
│   ├── alembic/
│   │   ├── versions/            # Database migration scripts
│   │   ├── env.py               # Alembic environment config
│   │   └── README
│   ├── src/
│   │   ├── api/                 # (Planned) API routes
│   │   ├── core/                # Core utilities & configs
│   │   ├── database/
│   │   │   ├── base.py          # Declarative Base
│   │   │   ├── session.py       # SQLAlchemy engine & session
│   │   │   └── models/          # ORM models (User, ChatSession, ChatSummary)
│   │   └── pipelines/           # RAG & processing pipelines (WIP)
│   ├── alembic.ini              # Alembic configuration
│   ├── main.py                  # Backend entry point
│   ├── mlflow.db                # MLflow tracking database
│   ├── requirement.txt          # Python dependencies
│   ├── test.py                  # Local testing utilities
│   └── .env                     # Environment variables (DB, API keys)
│
├── law_faiss_store/
│   ├── index.faiss              # FAISS vector index
│   ├── index.pkl                # Metadata store
│
├── Python_Notebooks/
│   ├── Docling_example.ipynb
│   └── Law_Summarizer_Notebook.ipynb
│
├── Raw Law Corpus/
│   ├── Markdown Files/          # Parsed legal text
│   └── PDF Files/               # Original legal documents
│
├── .gitignore
└── README.md
```

---

## 🗄️ Database Layer (Implemented ✅)

* **PostgreSQL** with SCRAM-SHA-256 authentication
* **SQLAlchemy ORM**
* **Alembic migrations**

### Core Tables

* `users` – authentication & roles
* `chat_sessions` – conversation tracking
* `chat_summaries` – AI-generated summaries
* `alembic_version` – migration state

This ensures:

* Secure data handling
* Persistent chat memory
* Expandable legal conversation architecture

---

## 🧠 AI & NLP Stack (In Progress 🚀)

* **LangChain** – LLM orchestration
* **Docling** – legal PDF → structured text
* **FAISS** – vector similarity search
* **MLflow** – experiment tracking
* **LLMs** – summarization & reasoning
* Domain detection for law classification

---

## 🧪 Research & Prototyping

* Jupyter notebooks used to:

  * Validate RAG workflows
  * Test summarization strategies
  * Experiment with legal document parsing
* Notebook logic is being **gradually migrated into `src/pipelines/`**

---

## 🛠️ Current Capabilities

* ✔ Backend architecture finalized
* ✔ Secure DB schema with migrations
* ✔ Chat session & summary modeling
* ✔ Vector store initialized
* ✔ Legal document parsing validated
* ✔ MLflow experiment tracking enabled

---

## 🔜 Roadmap / Next Steps

* 🔄 Complete document ingestion pipeline
* 🧠 Full RAG pipeline with conversation memory
* 🧾 Citation-aware legal responses
* 🔐 Authentication & role-based access
* 🌐 FastAPI-based REST API
* 🧪 Automated tests
* 📄 Research paper & technical documentation

---

## ⚠️ Disclaimer

NyayaConsult **does not provide legal advice**.
It is intended strictly for **research, educational, and assistance purposes**.

---

## 🤝 Contributions

The project is under active development.
Contributions and discussions will be welcomed once the core RAG pipeline stabilizes.

---
*Developed on Fedora Linux.*
