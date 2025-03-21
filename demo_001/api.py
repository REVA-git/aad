from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Basic FastAPI Demo",
    description="A simple API built with FastAPI",
    version="0.1.0",
)


# Pydantic model for item validation
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True


# In-memory database
items_db = {}
counter = 0


@app.get("/")
async def root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Welcome to the FastAPI demo API!"}


@app.get("/items", response_model=List[Item])
async def get_items():
    """Get all items from the database."""
    return list(items_db.values())


@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Get a specific item by ID."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]


@app.post("/items", response_model=Item)
async def create_item(item: Item):
    """Create a new item."""
    global counter
    counter += 1
    item.id = counter
    items_db[counter] = item
    return item


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    """Update an existing item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    item.id = item_id
    items_db[item_id] = item
    return item


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Delete an item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Item deleted successfully"}


# For running the application directly
if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
