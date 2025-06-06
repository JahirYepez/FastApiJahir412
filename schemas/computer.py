from pydantic import BaseModel, Field
from typing import Optional

class Computer(BaseModel):
    id:Optional[int] = None ###Indicar que es opcional
    brand:str = Field(max_length=100, min_length=2)
    model:str = Field(max_length=100, min_length=2)
    color:str = Field(max_length=100, min_length=2)
    ram:str = Field(max_length=100, min_length=2)
    storage:str = Field(max_length=100, min_length=2)

    class Config:
        json_schema_extra = {
            "example": {
                "brand": "Dell",
                "model": "XPS 13",
                "color": "Silver",
                "ram": "16GB",
                "storage": "512GB SSD"
            }
        }