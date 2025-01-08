# 백엔드 실습

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

users = {
    0: {"userid":"apple", "name":"김사과"},
    1: {"userid":"banana", "name":"반하나"},
    2: {"userid":"orange", "name":"오렌지"},
}
app = FastAPI()
# http://127.0.0.1:8000/users/0
@app.get("/users/{id}")
async def find_user(id: int):
    user = users[id]
    return user
# http://127.0.0.1:8000/users/1/userid
@app.get("/users/{id}/{key}")
async def find_user_by_key(id: int, key: str):
    user = users[id][key]
    return user
# http://127.0.0.1:8000/id-by-name?name=김사과
@app.get("/id-by-name")
async def find_user_by_name(name: str):
    for _, user in users.items():
        if user['name'] == name:
            return user
    return {"error": "데이터를 찾지 못함"}

class User(BaseModel):
    userid: str
    name: str

# http://127.0.0.1:8000/users/0 (X)
@app.post("/users/{id}")
async def create_user(id: int, user: User):
    if id in users:
        return {'error':'이미 존재하는 키'}
    users[id] = user.__dict__
    return {'sucess':'OK'}

# # http://127.0.0.1:8000/users/0 (X)
# @app.post("/users/{id}")
# def create_user(id: int, user: User):
#     if id in users:
#         return {"error": "이미 존재하는 키"}
#     users[id] = user.__dict__
#     return {"success":"ok"}

class UserforUpdate(BaseModel):
    userid: Optional[str] = None
    name: Optional[str] = None

@app.put('/users/{id}')
async def update_user(id: int, user: UserforUpdate):
    if id not in users:
        return{'error':'id가 존재하지 않음'}
    if user.userid:
        users[id]['userid'] = user.userid
    if user.name:
        users[id]['name'] = user.name
    return {'sucess':'OK'}

@app.delete('/users/{id}')
async def delete_user(id: int):
    users.pop(id)
    return {'sucess':'ok'}

# uvicorn main:app --reload