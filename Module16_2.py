from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/user/{username}/{age}")
async def id_paginator(
        username:Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
        age:Annotated[int, Path(ge=18, le=120, description="Enter age", example="75")],) -> dict:
        return {"message": f"Привет, {username}! Ваш возраст: {age}"}

@app.get("/user/{user_id}")
async def get_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", example="10")) -> dict:
    return {"Вы вошли как пользователь № user_id": user_id, "Dmitryi": f"User {user_id}"}

@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def news() -> dict:
    return {"message": "Вы вошли как администратор"}

