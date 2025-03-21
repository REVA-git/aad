# 001_demo-1

This demo consists of a basic FastAPI backend with an introduction to LangChain integration with Google's Gemini AI model.

## Current Implementation

### API Endpoints (api.py)

The demo currently implements a RESTful CRUD API for managing items:

- `GET /` - Welcome message
- `GET /items` - Get all items
- `GET /items/{item_id}` - Get a specific item
- `POST /items` - Create a new item
- `PUT /items/{item_id}` - Update an existing item
- `DELETE /items/{item_id}` - Delete an item

### AI Integration (ai.py)

The demo includes initial LangChain integration with Google's Gemini AI model:

- Uses `ChatGoogleGenerativeAI` with the `gemini-2.0-flash` model
- Implements a basic prompt template for question answering
- Demonstrates how to invoke the AI chain with a sample question

## Running the Demo

The API can be started by running from the root of the project:

```bash
 uv run uvicorn demo_001.api:app
```

This will start the service on `http://0.0.0.0:8000`
