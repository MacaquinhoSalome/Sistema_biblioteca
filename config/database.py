from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Models

# Configuración de la base de datos
DATABASE_URL = r"sqlite:///C:/Users/salom/Desktop/database/biblioteca.db" #ajustar segun sea el caso

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Models.Base.metadata.create_all(bind=engine)
