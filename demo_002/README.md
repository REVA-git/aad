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

# Exercises

Complete the following exercises to practice what you've learned:

## Exercise 1: Create a Specialized Assistant

Modify the existing prompt template to create a specialized assistant:

- Create a chef assistant that provides recipes and cooking advice
- Implement a tutor assistant that explains concepts in an educational manner
- Build a travel guide assistant that recommends destinations and activities

## Exercise 2: Implement Chat Memory

Enhance the chat functionality with conversation memory:

- Add conversation history tracking using LangChain's memory components
- Modify the API to maintain context across multiple messages
- Create a new endpoint that returns the conversation history

## Exercise 3: Add Streaming Response

Implement the planned streaming endpoint:

- Create a `POST /chat/stream` endpoint that streams responses from the LLM
- Implement proper handling of the streaming response in FastAPI
- Add a simple HTML interface that displays the streaming response in real-time

## Exercise 4: Create a Role-Based Assistant

Build an assistant with different personas:

- Allow users to specify a role for the assistant (e.g., "professional", "friendly", "concise")
- Create different prompt templates for each role
- Implement a router that selects the appropriate prompt based on the requested role

## Exercise 5: Build a Tool-Using Assistant

Extend the assistant with tool-using capabilities:

- Define simple tools like a calculator, weather lookup, or web search simulation
- Update the prompt template to instruct the model how to use these tools
- Implement the logic to process tool calls and feed results back to the model
