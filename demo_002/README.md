# 002_demo-2

This demo consists of a basic FastAPI AI backend with LangChain integration.
We have one implemented endpoint:

- POST /chat - Sends user messages to the LLM and returns AI responses

## Implementation Details

### API Endpoints (api.py)

The demo implements a simple chat API:

- `POST /chat` - Accepts a human message and returns an AI response

### AI Integration (ai.py)

The demo includes LangChain integration with Google's Gemini AI model:

- Uses `ChatGoogleGenerativeAI` with the `gemini-2.0-flash` model
- Implements a basic prompt template for question answering
- Creates a chain that connects the prompt template to the LLM

## Running the Demo

The API can be started by running from the root of the project:

```bash
uv run uvicorn demo_002.api:app --reload
```

This will start the service on `http://127.0.0.1:8000`
