from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session # instancias para la conexion de DB
from models.movie import Movie as MovieModel # modelos de archivo movie
from fastapi.encoders import jsonable_encoder # Para parsear de json a sql
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie


movie_router = APIRouter


@movie_router.get('/movies', tags=['Movies'], response_model= List[Movie], status_code= 200, dependencies=[Depends(JWTBearer())]) # Dependencies es para forzar la autenticacion previa
def get_movies() -> List[Movie]:
    db = Session() #iniciamos la sesion de linkeo a la DB
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content= jsonable_encoder(result)) # mostrar resultado json

@movie_router.get('/movies/{id}', tags=['Movies'], response_model= Movie, status_code=200, dependencies=[Depends(JWTBearer())])# Dependencies es para forzar la autenticacion previa
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db = Session() #iniciamos la sesion de linkeo a la DB
    result = MovieService(db).get_movie(id) # asignar a result, la movie con el mismo id (el primero con ese id, unico)
    if not result:
        return JSONResponse(status_code=404, content= []) # respuesta al no encontrar el id
    return JSONResponse(status_code= 200, content= jsonable_encoder(result)) # mostrar resultado json

@movie_router.get('/movie/', tags=['Movies'], response_model= List[Movie], status_code=200, dependencies=[Depends(JWTBearer())]) # Dependencies es para forzar la autenticacion previa
def get_movie_by_category(category:str = Query(min_length=5, max_length=50)) -> List[Movie]:
    db = Session() #iniciamos la sesion de linkeo a la DB
    result = MovieService(db).get_movies_by_category(category) # asignar a result, la movie con el mismo category (todos con ese)
    if not result:
        return JSONResponse(status_code=404, content= []) # respuesta al no encontrar una movie con esa category
    return JSONResponse(status_code= 200, content= jsonable_encoder(result)) # mostrar resultado json

@movie_router.post('/movies', tags=['Movies'], response_model= dict, status_code= 201, dependencies=[Depends(JWTBearer())]) # Dependencies es para forzar la autenticacion previa
def create_movie(movie: Movie) -> dict:

    db = Session() #iniciamos la sesion de linkeo a la DB
    MovieService(db).create_movie(movie)

    return JSONResponse(status_code=201, content= {"message": "Se ha registrado la pelicula"}) # mensaje de resultado correcto

@movie_router.delete('/movies/{id}', tags=['Movies'], response_model= dict, status_code= 200, dependencies=[Depends(JWTBearer())]) # Dependencies es para forzar la autenticacion previa
def delete_movie(id : int) -> dict:
    db = Session() #iniciamos la sesion de linkeo a la DB
    result = db.query(MovieModel).filter(MovieModel.id == id).first() # asignar a result, la movie con el mismo id (el primero con ese id, unico)
    if not result:
        return JSONResponse(status_code=404, content={"message":"No se encontrado"}) # mensaje de no id encontrado
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content= {"message": "Se ha eliminado la pelicula"}) # mensaje mostrado de todo correcto
    

@movie_router.put('/movies/{id}', tags=['Movies'], response_model= dict, status_code= 200, dependencies=[Depends(JWTBearer())]) # Dependencies es para forzar la autenticacion previa
def update_movie(id: int, movie: Movie) -> dict:
    db = Session() 
    result = MovieService(db).get_movie(id) 
    if not result:
        return JSONResponse(status_code=404, content= []) 
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code= 200, content={"message":"Se actualizo la pelicula"}) 
    