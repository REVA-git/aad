# AAD (Automated Application Development)

## Overview

AAD is a Python-based project that leverages FastAPI and LangChain for automated application development. This project provides a framework for building intelligent applications with modern AI capabilities, featuring a series of progressive demos that showcase different aspects of AI-powered application development.

## Demos

### [Demo 001](./demo_001) - FastAPI CRUD with Basic LangChain Integration

A foundational demo that implements:

- Complete CRUD API for item management
- Initial LangChain integration with Google's Gemini AI model
- Basic prompt templating and question answering capabilities
- Includes exercises for extending functionality with search, todos, and advanced AI features

### [Demo 002](./demo_002) - AI-Powered Chat Application

An advanced demo focusing on:

- Dedicated chat endpoint with LLM integration
- Enhanced LangChain implementation with Gemini AI
- Structured prompt templates for conversational AI
- Exercises for building specialized assistants, adding memory, and implementing streaming responses

## Project Structure

```
.
├── 000_setup/         # Initial setup and configuration files
├── demo_001/         # CRUD API with basic AI integration
│   ├── api.py       # FastAPI CRUD endpoints
│   ├── ai.py        # LangChain integration
│   └── README.md    # Demo-specific documentation
├── demo_002/         # Advanced AI chat implementation
│   ├── api.py       # Chat API endpoints
│   ├── ai.py        # Enhanced LangChain setup
│   └── README.md    # Demo-specific documentation
├── pyproject.toml    # Project dependencies and metadata
├── .env             # Environment variables configuration
└── .gitignore       # Git ignore rules
```

## Requirements

- Python >= 3.12
- Dependencies managed via `pyproject.toml`

## Key Dependencies

- FastAPI >= 0.115.11
- LangChain >= 0.3.21
- LangChain Community >= 0.3.20
- LangChain Google GenAI >= 2.1.0
- Python-dotenv >= 1.0.1
- Uvicorn >= 0.34.0

## Quick Start

1. Clone the repository:

```bash
git clone <repository-url>
cd aad
```

2. Set up Python environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:

```bash
pip install -e .
```

4. Configure environment variables:

- Copy `.env.example` to `.env` (if provided)
- Set required environment variables

5. Run a demo:

```bash
# For Demo 001
uv run uvicorn demo_001.api:app

# For Demo 002
uv run uvicorn demo_002.api:app --reload
```

## Development

Each demo in this project is designed to be self-contained and focuses on specific aspects of AI application development:

- **Demo 001** serves as an introduction to combining FastAPI with LangChain
- **Demo 002** builds upon the foundation to create a more sophisticated AI chat application

Each demo includes its own README with detailed documentation and exercises for further learning and development.

## License

[Add license information]

## Contributing

[Add contribution guidelines if applicable]
