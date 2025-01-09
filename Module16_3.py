from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_all_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int) -> dict:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return {"user_id": current_index, "message": f"User {current_index} is registered"}

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int) -> dict:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"user_id": user_id, "message": f"The user {user_id} is updated"}

@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> dict:
    del users[user_id]
    return {"user_id": user_id, "message": f"User {user_id} was deleted."}

