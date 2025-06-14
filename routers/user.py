from fastapi import APIRouter
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import User


user_router = APIRouter()


@user_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin": # validacion de credenciales
        token: str = create_token(user.dict()) # creacion del token de autorizacion
        return JSONResponse(status_code=200, content=token) # mostrar el token para validarnos