from pydantic import BaseModel

# clase modelo del usuario (credenciales necesarias)
class User(BaseModel):
    email: str
    password: str
    # Esto es para debugear mas rapido (no debe de existir)
    class Config:
        json_schema_extra = {
            "example": {
                "email": "admin@gmail.com",
                "password": "admin"
            }
        }