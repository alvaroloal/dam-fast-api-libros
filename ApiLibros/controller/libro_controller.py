from fastapi import APIRouter, HTTPException
from typing import List
from model.libro_model import Libro
from service.libro_service import LibroService

router = APIRouter(
    tags=["Libros"]
)
service = LibroService()

@router.get("/libros", response_model=List[Libro],summary="Obtener todos los libros", description="Devuelve una lista de todos los libros disponibles en la base de datos.")
def get_libros():
    return service.get_all_libros()

@router.get("/libros/{libro_id}", response_model=Libro,summary="Obtener un libro por ID", description="Devuelve un libro específico basado en el ID proporcionado.", responses={404: {"description": "Libro no encontrado"}})
def get_libro(libro_id: int):
    libro = service.get_libro_by_id(libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro

@router.post("/libros", response_model=Libro, summary="Crear un nuevo libro", description="Crea un nuevo libro en la base de datos con la información proporcionada.", responses={201: {"description": "Libro creado exitosamente"}})
def create_libro(libro: Libro):
    return service.create_libro(libro)

@router.put("/libros/{libro_id}", response_model=Libro, summary="Actualizar un libro", description="Actualiza la información de un libro existente basado en el ID proporcionado.", responses={404: {"description": "Libro no encontrado"}})
def update_libro(libro_id: int, updated_libro: Libro):
    libro = service.update_libro(libro_id, updated_libro)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro

@router.delete("/libros/{libro_id}", response_model=Libro, summary="Eliminar un libro", description="Elimina un libro de la base de datos basado en el ID proporcionado.", responses={404: {"description": "Libro no encontrado"}})
def delete_libro(libro_id: int):
    libro = service.delete_libro(libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro