from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Modelo para la tabla de libros
class Libro(Base):
    __tablename__ = "libros"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    editorial = Column(String, nullable=False)
    anio = Column(Integer, nullable=False)

# Modelo para la tabla de usuarios
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    identificacion = Column(String, unique=True, nullable=False)

# Modelo para la tabla de préstamos
class Prestamo(Base):
    __tablename__ = "prestamos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    libro_id = Column(Integer, ForeignKey("libros.id"), nullable=False)
    usuario = relationship("Usuario")
    libro = relationship("Libro")
