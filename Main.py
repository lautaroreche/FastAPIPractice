# Documentation with Swagger: http://127.0.0.1:8000/docs
# Documentation with Redocly: http://127.0.0.1:8000/redoc


from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    id: int
    first_name: str
    last_name: str

class UserToDelete(BaseModel):
    id: int


app = FastAPI()
users = []


@app.get('/users')
def get_users() -> list[User]:
    return users


# Search user by query
@app.get('/users/')
def get_users_query(id: int = None, first_name: str = None, last_name: str = None) -> Union[list[User], User, dict]:
    filtered_users = []
    if id is None and first_name is None and last_name is None:
        return users
    for user in users:
        if id in [user['id'], None] and first_name in [user['first_name'], None] and last_name in [user['last_name'], None]:
            filtered_users.append(user)
    if len(filtered_users) > 1:
        return filtered_users
    elif len(filtered_users) == 1:
        return filtered_users[0]
    return {'message': 'User not found'}


# Search user indicating id
@app.get('/users/{id}')
def get_users_indicate_id(id: int) -> Union[User, dict]:
    for user in users:
        if user['id'] == id:
            return user
    return {'message': 'User not found'}


@app.post('/users')
def create_user(user_obj: User) -> dict:
    users.append(user_obj.model_dump())
    return {'message': 'User created successfully'}


@app.put('/users')
def update_user(user_obj: User)  -> dict:
    for user in users:
        if user['id'] == user_obj.id:
            user['first_name'] = user_obj.first_name
            user['last_name'] = user_obj.last_name
            return {'message': 'User modified successfully'}
    return {'message': 'User not found'}


@app.delete('/users')
def delete_user(user_obj: UserToDelete)  -> dict:
    for user in users:
        if user['id'] == user_obj.id:
            users.remove(user)
            return {'message': 'User deleted successfully'}
    return {'message': 'User not found'}


# Run from terminal: uvicorn fastAPI:app --reload
# Consult in browser: http://127.0.0.1:8000/users
