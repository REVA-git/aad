from fastapi import FastAPI
from langchain_core.messages import HumanMessage, AIMessage
from pydantic import BaseModel
import uvicorn
from .ai import chain

# Initialize FastAPI app
app = FastAPI(
    title="Basic FastAPI with Langchain",
    description="A simple API built with FastAPI and Langchain",
    version="0.1.0",
)


# Pydantic model for item validation
class Message(BaseModel):
    content: str


@app.post("/chat", response_model=AIMessage)
async def chat(message: HumanMessage):
    """basic chat endpoint"""
    return chain.invoke({"question": message.content})


# For running the application directly
if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
