from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, Dict

app = FastAPI()

users: Dict[int, str] = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_all_users():
    return users

@app.post("/user/{username}/{age}")
async def create_user(
        username:Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
        age:Annotated[int, Path(ge=18, le=120, description="Enter age", example="75")],):
        next_id = str(int(max(users.keys())) + 1)
        users[next_id] = f"Имя: {username}, возраст: {age}"
        return {"message": f"User {next_id} is registered"}

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id:Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="10")],
        username:Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
        age:Annotated[int, Path(ge=18, le=120, description="Enter age", example="75")],):
        if str(user_id) not in users:
            raise HTTPException(status_code=404, detail="User not found")
        users[str(user_id)] = f"Имя: {username}, возраст: {age}"
        return {"message": f"The user {user_id} is updated"}

@app.delete("/user/{user_id}")
async def delete_user(user_id:Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="10")]):
    if str(user_id) not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[str(user_id)]
    return {"message": f"User {user_id} was deleted."}

