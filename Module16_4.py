from fastapi import FastAPI, Path, status, Body, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/users", response_model=List[User])
async def get_all_users():
    return users

@app.post("/user/{username}/{age}", response_model= User, status_code=201)
async def create_user(username: str, age: int):
    next_id = 1 if not users else users[-1].id + 1
    new_user = User(id=next_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}", response_model= User)
async def update_user(user_id: int, username: str, age: int):
    try:
        user_index = users.index(next((user for user in users if user.id == user_id), None))
        users[user_index] = User(id=user_id, username=username, age=age)
        return users[user_index]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}", response_model= User)
async def delete_user(user_id: int):
    try:
        user_index = users.index(next((user for user in users if user.id == user_id), None))
        return users.pop(user_index)
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")