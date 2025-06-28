from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import FileResponse

app = FastAPI()

# Banco de dados em memória
fake_todos_db = []


class Todo(BaseModel):
    title: str
    description: str | None = None

@app.get("/")
def read_root():
    return {"message": "Vamos de TDD!"}


@app.post("/todos/")
def create_todo(todo: Todo):
    todo_data = todo.model_dump()
    fake_todos_db.append(todo_data)
    return {"message": "Todo criado!", "todo": todo_data}


@app.get("/todos/")
def read_todos():
    return {"todos": fake_todos_db}