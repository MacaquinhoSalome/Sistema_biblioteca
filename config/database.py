from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Models

# Configuración de la base de datos
DATABASE_URL = "postgresql://postgres:simian2003@localhost:5433/biblioteca"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Models.Base.metadata.create_all(bind=engine)
