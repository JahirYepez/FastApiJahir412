from fastapi import FastAPI
from config.database import engine, Base # instancias para la conexion de DB
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.computer import computer_router
from routers.user import user_router


# from fastapi.responses import HTMLResponse 
### http://127.100.0.7:8000/docs#/    ruta para correr
### uvicorn main:app --reload --port 8000 --host 127.100.0.7

app = FastAPI() ###Variable para ejecutar la instancia de FastAPI
app.title = "Mi primera vaplicacion con FastAPI" ### titulo que mostrara el proyecto
app.version ="0.0.1"  ### version del programa a mostrar

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(computer_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine) # iniciar la DB

@app.get('/', tags=['home'])
def message():
    return"Hello World"


### creacion de la lista de las computadoras
computers = [
    {
        "id": 1,
        "brand": "Dell",
        "model": "XPS 13",
        "color": "Silver",
        "ram": "16GB",
        "storage": "512GB SSD"
    },
    {
        "id": 2,
        "brand": "Apple",
        "model": "MacBook Pro",
        "color": "Space Gray",
        "ram": "32GB",
        "storage": "1TB SSD"
    },
    {
        "id": 3,
        "brand": "HP",
        "model": "Pavilion 15",
        "color": "Black",
        "ram": "8GB",
        "storage": "256GB SSD"
    },
    {
        "id": 4,
        "brand": "Lenovo",
        "model": "ThinkPad X1 Carbon",
        "color": "Black",
        "ram": "16GB",
        "storage": "512GB SSD"
    },
    {
        "id": 5,
        "brand": "Asus",
        "model": "ROG Zephyrus G14",
        "color": "White",
        "ram": "32GB",
        "storage": "1TB SSD"
    },
    {
        "id": 6,
        "brand": "Acer",
        "model": "Swift 3",
        "color": "Blue",
        "ram": "8GB",
        "storage": "512GB SSD"
    },
    {
        "id": 7,
        "brand": "Microsoft",
        "model": "Surface Laptop 4",
        "color": "Platinum",
        "ram": "16GB",
        "storage": "512GB SSD"
    },
    {
        "id": 8,
        "brand": "Razer",
        "model": "Blade 15",
        "color": "Black",
        "ram": "32GB",
        "storage": "1TB SSD"
    },
    {
        "id": 9,
        "brand": "MSI",
        "model": "GS66 Stealth",
        "color": "Black",
        "ram": "32GB",
        "storage": "1TB SSD"
    },
    {
        "id": 10,
        "brand": "MSI",
        "model": "Pixelbook Go",
        "color": "Pink",
        "ram": "16GB",
        "storage": "256GB SSD"
    }
]



