from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Computer(Base):
    __tablename__ = "computers"

    id = Column(Integer, primary_key = True)
    brand = Column(String)
    model = Column(String)
    color = Column(String)
    ram = Column(String)
    storage = Column(String)
    