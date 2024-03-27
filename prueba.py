# Documentation with Swagger: http://127.0.0.1:8000/docs
# Documentation with Redocly: http://127.0.0.1:8000/redoc
from fastapi import FastAPI, Body

app = FastAPI()

users = [
    {
        'id': 1,
        'first_name': 'First',
        'last_name': 'User'
    },
    {
        'id': 2,
        'first_name': 'Second',
        'last_name': 'User'
    }
]


@app.get('/users')
def get_users():
    return users


# Search user by query
@app.get('/users/')
def get_users_query(id: int = None, first_name: str = None, last_name: str = None):
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
def get_users_indicate_id(id: int):
    for user in users:
        if user['id'] == id:
            return user
    return {'message': 'User not found'}


@app.post('/users')
def create_user(id: int = Body(), first_name: str = Body(), last_name: str = Body()):
    users.append({
        'id': id,
        'first_name': first_name,
        'last_name': last_name
    })
    return {'message': 'User created successfully'}


@app.put('/users/{id}')
def update_user(id: int, first_name: str = Body(), last_name: str = Body()):
    for user in users:
        if user['id'] == id:
            user['first_name'] = first_name
            user['last_name'] = last_name
            return {'message': 'User modified successfully'}
    return {'message': 'User not found'}


@app.delete('/users/{id}')
def delete_user(id: int):
    for user in users:
        if user['id'] == id:
            users.remove(user)
            return {'message': 'User deleted successfully'}
    return {'message': 'User not found'}


# Ejecutar desde terminal: uvicorn prueba:app --reload
# Consultar en navegador: http://127.0.0.1:8000/users
    