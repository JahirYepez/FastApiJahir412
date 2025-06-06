from config.database import Base # la base de datos configurada
from sqlalchemy import Column, Integer, String, Float # metodos y tipos de datos para la creacion de tabla

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)