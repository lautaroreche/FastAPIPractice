# Documentación son Swagger: http://127.0.0.1:8000/docs
# Documentación son Redocly: http://127.0.0.1:8000/redoc
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    id: int
    nombre: str
    apellido: str


users_list = [User(id = 1, nombre = "Lautaro", apellido = "Reche"),
             User(id = 2, nombre = "Nilda Raquel", apellido = "Guardia"),
             User(id = 3, nombre = "Jorge", apellido = "Reche"),
             User(id = 4, nombre = "Agustín", apellido = "Reche"),
             User(id = 5, nombre = "Ramiro", apellido = "Reche"),
             User(id = 6, nombre = "Facundo", apellido = "Reche"),
             User(id = 7, nombre = "Marcelo Jorge", apellido = "Reche"),
             User(id = 8, nombre = "Laura María", apellido = "González"),
             User(id = 9, nombre = "Gustavo Javier", apellido = "Merodio"),
             User(id = 10, nombre = "Thiago Nicolás", apellido = "Merodio Romagnoli")]


def buscarUsuario(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"message": "No se ha encontrado el usuario"}


@app.get("/user/all")
async def users():
    return users_list


@app.get("/user/{id}")
async def user(id: int):
    return buscarUsuario(id)


@app.post("/user/", status_code = 201)
async def user(user: User):
    if type(buscarUsuario(user.id)) == User:
        raise HTTPException(status_code = 204, detail = "El usuario ya existe")
    else:
        users_list.append(user)
        return {"message": "El usuario fue añadido con exito"}
    

@app.put("/user/", status_code = 201)
async def user(user: User):
    for index, usuarioModificar in enumerate(users_list):
        if usuarioModificar.id == user.id:
            users_list[index] = user
            return {"message": "El usuario fue modificado con exito"}
    raise HTTPException(status_code = 204, detail = "No se ha encontrado el usuario")


@app.delete("/user/{id}")
async def user(id: int):
    for index, usuarioEliminar in enumerate(users_list):
        if usuarioEliminar.id == id:
            del users_list[index]
            return {"message": "El usuario fue eliminado con exito"}
    raise HTTPException(status_code = 204, detail = "No se ha encontrado el usuario")


# Ejecutar desde terminal: uvicorn main:app --reload
# Consultar en navegador: http://127.0.0.1:8000/user/{id}