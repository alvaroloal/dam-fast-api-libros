from typing import List, Optional
from model.libro_model import Libro
from repository.libro_repository import LibroRepository

class LibroService:
    def __init__(self):
        self.repository = LibroRepository()

    def get_all_libros(self) -> List[Libro]:
        return self.repository.get_all_libros()

    def get_libro_by_id(self, libro_id: int) -> Optional[Libro]:
        return self.repository.get_libro_by_id(libro_id)

    def create_libro(self, libro: Libro) -> Libro:
        return self.repository.create_libro(libro)

    def update_libro(self, libro_id: int, updated_libro: Libro) -> Optional[Libro]:
        return self.repository.update_libro(libro_id, updated_libro)

    def delete_libro(self, libro_id: int) -> Optional[Libro]:
        return self.repository.delete_libro(libro_id)