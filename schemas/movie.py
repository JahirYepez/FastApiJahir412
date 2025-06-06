from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id:Optional[int] = None ###Indicar que es opcional
    title:str = Field(max_length=100, min_length=5)
    overview:str = Field(min_length=5, max_length=100)
    year: int = Field(le=2025)
    rating: float = Field(ge=1, le=10)
    category:str = Field(min_length=5, max_length=100)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Mi pelicula",
                "overview": "Descripcion de la pelicula",
                "year": 2025,
                "rating": 6.6,
                "category": "Action"
            }
        }