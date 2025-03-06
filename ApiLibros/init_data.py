from model.libro_model import Libro
from service.libro_service import LibroService

def create_sample_data():
    service = LibroService()
    
    sample_libros = [
        Libro(titulo="Libro 1", autor="Autor 1", descripcion="Descripcion libro 1", disponible=False),
        Libro(titulo="Libro 2", autor="Autor 2", descripcion="Descripcion libro 2", disponible=True),
        Libro(titulo="Libro 3", autor="Autor 3", descripcion="Descripcion libro 3", disponible=False)
    ]
    
    for libro in sample_libros:
        service.create_libro(libro)

if __name__ == "__main__":
    create_sample_data()