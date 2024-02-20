from typing import Union
import uvicorn
from fastapi import FastAPI

# import requests
# import json


app = FastAPI()


todos = [
    {
        "id": "1",
        "Activity": "Running"
    },  
    {
        "id": "2",
        "Activity": "Walking"
    }
]


# A minimal app to demonstrate the get request
@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Ping:": "Pong"}


# Get --> Read Todo
@app.get("/todo", tags=['Todos'])
async def get_todos() -> dict:
    return {"Data": todos}


# Post --> Create Todo  
@app.post("/todo", tags=["Todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": "A Todo is Added!"
    }
    
# Put --> Update Todo
@app.put("/todo/{id}", tags=["Todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if (int(todo["id"])) == id:
            todo["Activity"] = body["Activity"]
            return {
                "data": f"Todo with id {id} has been updated"
            }
    return {
        "data": f"This Todo with id {id} is not found!"
    }
    
# DELETE --> Delete Todo
@app.delete("/todo/{id}", tags=["Todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return{
                "data": f"Todo with id {id} has been deleted!"
            }
    return {
        "data": f"Todo with id {id} as not found!"
    }


# act = {"id": "3","Activity" : "Play football"}
# r = requests.post("http://127.0.0.1:8000/todo", data=json.dumps(act))
# print(r)
# print(r.json())

# act = {"id": "3","Activity" : "Play games"}
# r = requests.post("http://127.0.0.1:8000/todo", data=json.dumps(act))
# print(r)
# print(r.json())

# r = requests.get("http://127.0.0.1:8000/todo")
# print(r)
# print(r.json())