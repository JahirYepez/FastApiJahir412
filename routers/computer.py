from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session # instancias para la conexion de DB
from models.computer import Computer as ComputerModel # modelos de archivo computer
from fastapi.encoders import jsonable_encoder # Para parsear de json a sql
from middlewares.jwt_bearer import JWTBearer
from services.computer import ComputerService
from schemas.computer import Computer


computer_router = APIRouter


### ENDPOINT para obtener todas las computadoras
@computer_router.get('/computers', tags=['Computers'], response_model= List[Computer], status_code= 200, dependencies=[Depends(JWTBearer())]) # Dependencies es para forzar la autenticacion previa
def get_computers() -> List[Computer]:
    db = Session() #iniciamos la sesion de linkeo a la DB
    result = ComputerService(db).get_computers() # Asignamos todos los computers en la DB a result
    return JSONResponse(status_code=200, content= jsonable_encoder(result)) # mostrar resultado json

### ENDPOINT para obtener una computadora mediante su ID
@computer_router.get('/computers/{id}', tags=['Computers'], response_model= Computer, status_code= 200, dependencies=[Depends(JWTBearer())]) # Dependencies es para forzar la autenticacion previa
def get_computer(id: int = Path(ge=1, le=2000)) -> Computer: 
    db = Session() #iniciamos la sesion de linkeo a la DB
    result = ComputerService(db).get_computer(id) # asignar a result, la computer con el mismo id (el primero con ese id, unico)
    if not result:
        return JSONResponse(status_code=404, content= []) # respuesta al no encontrar el id
    return JSONResponse(status_code= 200, content= jsonable_encoder(result)) # mostrar resultado json

### ENDPOINT para obtener las computadoras segun su marca
@computer_router.get('/computer/', tags=['Computers'], response_model= List[Computer], status_code= 200, dependencies=[Depends(JWTBearer())]) # Dependencies es para forzar la autenticacion previa
def get_computer_by_brand(brand:str = Query(min_length=2, max_lenfth=50)) -> List[Computer]: 
    db = Session() #iniciamos la sesion de linkeo a la DB
    result = ComputerService(db).get_computer_by_brand(brand) # asignar a result, las computers con el mismo brand (todos con ese brand)
    if not result:
        return JSONResponse(status_code=404, content= [])  # respuesta al no encontrar el id
    return JSONResponse(status_code= 200, content= jsonable_encoder(result)) # mostrar resultado json

### Metodo Post para computadoras
@computer_router.post('/computer', tags=['Computers'], response_model= dict, status_code= 200, dependencies=[Depends(JWTBearer())]) # Dependencies es para forzar la autenticacion previa
def create_computer(computer: Computer)-> dict:
    db = Session() #iniciamos la sesion de linkeo a la DB
    # Utilizamos el modelo  y le pasamos la inforacion que vamos a registrar
    new_computer = ComputerModel(**computer.model_dump())
    # Añadimos a la base de datos la pelicula
    db.add(new_computer)
    # Guardamos los datos
    db.commit()
    return JSONResponse(status_code=201, content= {"message": "Se ha registrado la computadora"}) # mensaje de todo correcto

### Metodo delete para computadoras
@computer_router.delete('/computer/{id}', tags=['Computers'], response_model= dict, status_code= 200, dependencies=[Depends(JWTBearer())]) # Dependencies es para forzar la autenticacion previa
def delete_computer(id : int = Path(ge=1, le=2000)) -> dict:
    db = Session() #iniciamos la sesion de linkeo a la DB
    result = db.query(ComputerModel).filter(ComputerModel.id == id).first() # asignar a result, la computer con el mismo id (el primero con ese id, unico)
    if not result:
        return JSONResponse(status_code=404, content={"message":"No se encontrado"}) # respuesta al no encontrar el id
    ComputerService(db).delete_computer(id)
    return JSONResponse(status_code=200, content= {"message": "Se ha eliminado la computadora"}) # mensaje de todo correcto
    
### Metodo put de computadoras
@computer_router.put('/computers/{id}', tags=['Computers'], response_model= dict, status_code= 200, dependencies=[Depends(JWTBearer())]) # Dependencies es para forzar la autenticacion previa
def update_computer(id: int, computer: Computer) -> dict: 
    db = Session() #iniciamos la sesion de linkeo a la DB
    result = ComputerService(db).get_computer(id)
    if not result:
        return JSONResponse(status_code=404, content= []) 
    ComputerService(db).update_computer(id, computer)
    return JSONResponse(status_code= 200, content={"message":"Se actualizo la computadora"}) # mensaje de todo correcto
