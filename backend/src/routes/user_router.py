from typing import List
from fastapi import Path, Query, APIRouter
from fastapi.responses import JSONResponse
from src.models.users_models import User

user_router = APIRouter()

# Listar todos los usuarios
@user_router.get('/', tags=['Users'], status_code=200, response_description='Successful Response...')
def get_users():
    content = []
    return JSONResponse(content = content, status_code=200)

# Obtener un usuario
@user_router.get('/{id}', tags=['Users'])
def get_user(id: int= Path(ge=0)):
    for movie in dbmovies:
        if movie.id == id:
            return JSONResponse(content = movie.model_dump(), status_code=200)
    return JSONResponse(content = {}, status_code=404)

# Buscar y borrar usuario
@user_router.delete('/{id}', tags=['Users'])
def delete_user(id: int=Path(ge=0) ):
    for user in dbuser:
        if user.id == id:
            dbuser.remove(user)
    content = [user.model_dump() for users in dbusers ]
    return JSONResponse(content = content, status_code=200)
