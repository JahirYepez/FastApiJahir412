import os # maneja variables de entorno URL
from sqlalchemy import create_engine # conexion entre base de datos y python
from sqlalchemy.orm.session import sessionmaker # genera fabrica de sesiones para la DB
from sqlalchemy.ext.declarative import declarative_base # definir modelos desde python

sqlite_file_name = "../database.sqlite"

#Estamos leyendo el directorio actual que es database.py
base_dir = os.path.dirname(os.path.realpath(__file__))

# Creamos la URL de la base de datos uniendo las 2 variables anteriores
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()