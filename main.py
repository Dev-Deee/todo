from typing import Optional, List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

import services

app = FastAPI()

class Todo(BaseModel):
    todo_id: int
    description: str
    completed: bool = False


class TodoCreate(BaseModel):
    title: str
    description: str

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


@app.get("/todos")
async def read_todos():
    return todos

@app.post("/todos")
async def create_todo(todo_create: TodoCreate):
    return services
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)