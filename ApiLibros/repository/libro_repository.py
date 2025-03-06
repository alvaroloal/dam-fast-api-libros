from typing import List, Optional
from model.libro_model import Libro


libros_db = [
    Libro(id=1, titulo="Harry Potter y la piedra filosofal", autor="J.K. Rowling", descripcion="El primer libro de Harry Potter", disponible=True),
    Libro(id=2, titulo="El Señor de los Anillos: La Comunidad del Anillo", autor="J.R.R. Tolkien", descripcion="El primer libro de El Señor de los Anillos", disponible=True),
    Libro(id=3, titulo="Harry Potter y la cámara secreta", autor="J.K. Rowling", descripcion="El segundo libro de Harry Potter", disponible=False),
    Libro(id=4, titulo="El Señor de los Anillos: Las dos torres", autor="J.R.R. Tolkien", descripcion="El segundo libro de El Señor de los Anillos", disponible=True),
    Libro(id=5, titulo="Harry Potter y el prisionero de Azkaban", autor="J.K. Rowling", descripcion="El tercer libro de Harry Potter", disponible=True),
]

class LibroRepository:
    def get_all_libros(self) -> List[Libro]:
        return libros_db

    def get_libro_by_id(self, libro_id: int) -> Optional[Libro]:
        return next((libro for libro in libros_db if libro.id == libro_id), None)

    def create_libro(self, libro: Libro) -> Libro:
        libros_db.append(libro)
        return libro

    def update_libro(self, libro_id: int, updated_libro: Libro) -> Optional[Libro]:
        libro = self.get_libro_by_id(libro_id)
        if libro:
            libro.titulo = updated_libro.titulo
            libro.autor = updated_libro.autor
            libro.descripcion = updated_libro.descripcion
            libro.disponible = updated_libro.disponible
        return libro

    def delete_libro(self, libro_id: int) -> Optional[Libro]:
        libro = self.get_libro_by_id(libro_id)
        if libro:
            libros_db.remove(libro)
        return libro