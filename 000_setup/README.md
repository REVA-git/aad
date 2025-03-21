# Tech Stack

Tech stack is the set of tools and technologies that you use for a particular project

### **Python Tech Stacks**

- **Django Stack** (Django, PostgreSQL/MySQL, React/Vue, Celery, Redis)
- **FastAPI Stack** (FastAPI, PostgreSQL, SQLAlchemy, React/Vue)
- **LangChain/LangGraph Stack** (LangChain/LangGraph, OpenAI/LLM, FastAPI, Pinecone/ChromaDB, Streamlit/Gradio)

### **JavaScript Tech Stacks**

- **MERN** (MongoDB, Express.js, React, Node.js)
- **MEAN** (MongoDB, Express.js, Angular, Node.js)
- **JAMstack** (JavaScript, APIs, Markup)
- **T3 Stack** (Next.js, TypeScript, tRPC, Prisma, Tailwind CSS)
- **Supabase Stack** (Supabase, PostgreSQL, Next.js/React, Prisma)

### **What we will use**

- Python - uv, FastAPI, LangChain/LangGraph, Supabase (Postgresql), SQLAlchemy
- Javascript/Typescript - Next.js (v0.dev)
- Cursor IDE
- AI Assistants - ChatGPT, Gemini, Perplexity, Cursor

### **IDE Setup - What is cursor? How to use it?**

- tools
- mcp
- cursorrules

### **Python setup**

- dependency management with uv https://docs.astral.sh/uv/
- what are pyproject.toml, uv.lock files?

### **Primary skillset to develop**

- Ability to learn new things and enduring discomfort.
- High Level Thinking
- System Design & Architecture
- Understanding of UI/UX Design
- Effective Prompting, being incharge

### **Software Backend Architecture vs. AI Backend Architecture**

Both **Software Backend Architecture** and **AI Backend Architecture** involve designing the system’s backend, but AI-driven applications have additional complexities related to model handling, inference, and data pipelines.

---

### **1. Software Backend Architecture**

Used for general web or mobile applications, focusing on handling requests, business logic, database management, and APIs.

#### **Key Components:**

- **API Layer** – Exposes endpoints via REST or GraphQL.
- **Business Logic Layer** – Implements rules, authentication, and workflows.
- **Database Layer** – Uses relational (PostgreSQL, MySQL) or NoSQL (MongoDB) databases.
- **Caching & Queues** – Uses Redis, RabbitMQ, or Kafka for efficiency.
- **Scalability** – Uses containerization (Docker, Kubernetes) for scaling.

#### **Example Tech Stack:**

- **Frameworks:** FastAPI, Django, Express.js, NestJS
- **Database:** PostgreSQL, MongoDB, MySQL
- **Caching & Queues:** Redis, Celery, Kafka
- **Auth & Security:** OAuth, JWT, Role-Based Access Control

---

### **2. AI Backend Architecture**

Used for AI-powered applications, requiring model deployment, inference optimization, and vector databases.

#### **Key Components:**

- **Model Serving Layer** – Uses FastAPI, Flask, TensorFlow Serving, or Triton Inference Server.
- **LLM Orchestration** – Uses LangChain/LangGraph for managing AI workflows.
- **Vector Databases** – Uses Pinecone, ChromaDB, or Weaviate for embeddings.
- **Retrieval Augmented Generation (RAG)** – Enhances LLM responses with real-time data.
- **Streaming & Real-time Processing** – Uses Kafka or WebSockets for real-time AI interactions.

#### **Example Tech Stack:**

- **Frameworks:** FastAPI, LangChain, Hugging Face Transformers
- **Model Hosting:** OpenAI API, Together AI, Groq
- **Vector DBs:** ChromaDB, Pinecone
- **Storage:** Supabase, PostgreSQL, S3

---

### **Key Differences:**

| Feature      | Software Backend                  | AI Backend                       |
| ------------ | --------------------------------- | -------------------------------- |
| Focus        | Handling business logic & APIs    | Model inference & AI workflows   |
| Data Storage | Relational/NoSQL DBs              | Vector DBs & embeddings          |
| Scaling      | Horizontal scaling via containers | GPU-based scaling for inference  |
| Optimization | Caching & indexing                | Model quantization, distillation |
| APIs         | REST, GraphQL                     | OpenAI API, LangChain pipelines  |

For generic applications we will need a mix of both:

- **FastAPI** (for backend APIs)
- **LangChain/LangGraph** (for AI logic and orchestration)
- **Supabase** (for structured storage)
- **Vector DB** (if you use embeddings for smart retrieval)
