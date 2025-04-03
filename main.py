from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

# Crear la app FastAPI
app = FastAPI()

# Configurar Jinja2 para servir plantillas
templates = Jinja2Templates(directory="templates")

# Montar la carpeta static para archivos CSS e imágenes
app.mount("/static", StaticFiles(directory="static"), name="static")

# Estructuras de datos
libros = []  # Lista para almacenar libros
usuarios = []  # Lista para almacenar usuarios
prestamos = []  # Lista para almacenar préstamos

# Modelos de datos
class Libro(BaseModel):
    titulo: str
    autor: str
    isbn: str
    editorial: str
    anio: int

class Usuario(BaseModel):
    nombre: str
    identificacion: str

# Ruta para la página de inicio
@app.get("/", response_class=HTMLResponse)
def leer_inicio(request: Request):
    return templates.TemplateResponse("inicio.html", {"request": request})

# Rutas para la gestión de libros
@app.get("/libros", response_class=HTMLResponse)
def leer_libros(request: Request):
    return templates.TemplateResponse("libros.html", {"request": request, "libros": libros})

@app.post("/libros")
def agregar_libro(
    titulo: str = Form(...), 
    autor: str = Form(...), 
    isbn: str = Form(...), 
    editorial: str = Form(...), 
    anio: int = Form(...)
):
    for libro in libros:
        if libro["isbn"] == isbn:  # Validar que el ISBN no sea duplicado
            raise HTTPException(status_code=400, detail="El ISBN ya existe.")
    nuevo_libro = {"titulo": titulo, "autor": autor, "isbn": isbn, "editorial": editorial, "anio": anio}
    libros.append(nuevo_libro)
    return templates.TemplateResponse("libros.html", {"request": {}, "libros": libros})

# Rutas para la gestión de usuarios
@app.get("/usuarios", response_class=HTMLResponse)
def leer_usuarios(request: Request):
    return templates.TemplateResponse("usuarios.html", {"request": request, "usuarios": usuarios})

@app.post("/usuarios")
def agregar_usuario(
    nombre: str = Form(...), 
    identificacion: str = Form(...)
):
    nuevo_usuario = {"nombre": nombre, "identificacion": identificacion}
    usuarios.append(nuevo_usuario)
    return templates.TemplateResponse("usuarios.html", {"request": {}, "usuarios": usuarios})

# Rutas para la gestión de préstamos
@app.get("/prestamos", response_class=HTMLResponse)
def leer_prestamos(request: Request):
    
    return templates.TemplateResponse("prestamos.html", {"request": request, "prestamos": prestamos})



@app.post("/prestamos")
def agregar_prestamos(
    libro: str = Form(...), 
    usuario: str = Form(...)
):
    nuevo_prestamo = {"libro": libro, "usuario": usuario}
    prestamos.append(nuevo_prestamo)
    return templates.TemplateResponse("prestamos.html", {"request": {}, "prestamos": prestamos})




""""
Guardar -- insert
actualizar -- update
leer en pantalla -- select
eliminar -- delete

"""