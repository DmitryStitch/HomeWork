from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{user_id}")
async def get_user(user_id: int) -> dict:
    return {"Вы вошли как пользователь № user_id": user_id, "Dmitryi": f"User {user_id}"}

@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def news() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user")
async def id_paginator(username: str = "Dmitry", age: int = 32) -> dict:
    return {"Информация о пользователе. " "Имя": username, "Возраст": age}