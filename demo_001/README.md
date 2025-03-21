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

# Exercises

Complete the following exercises to practice what you've learned:

## Exercise 1: Extend the Item API

Add the following features to the existing Item API:

- Add a `GET /items/search` endpoint that accepts a query parameter to search items by name
- Add a `quantity` field to the Item model with appropriate validation
- Add a `PATCH /items/{item_id}` endpoint that allows partial updates to an item

## Exercise 2: Create a Basic Todo API

Create a new set of endpoints for a Todo application:

- Define a Todo model with fields: id, title, description, completed, due_date
- Implement CRUD operations for todos similar to the Item API
- Add an additional endpoint to mark todos as completed

## Exercise 3: Integrate LangChain

Create a new endpoint that uses LangChain and Gemini:

- Add a `POST /summarize` endpoint that accepts text input
- Use LangChain with Gemini to generate a summary of the provided text
- Return both the original text and the summary

## Exercise 4: Build a Simple Question-Answering API

Create an API for a question-answering system:

- Add a `POST /ask` endpoint that accepts a question
- Use the LangChain setup from ai.py to answer the question
- Enhance the prompt template to instruct the model to respond in a specific format

## Exercise 5: Combine FastAPI and LangChain

Create a more complex application that combines both components:

- Build a `POST /analyze` endpoint that accepts a product description
- Use LangChain to analyze the text and extract key features and sentiment
- Store the analysis results using the Item API endpoints you built earlier
