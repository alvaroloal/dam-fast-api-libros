from pydantic import BaseModel
from typing import Optional

class Libro(BaseModel):
    id: int
    titulo: str
    autor: str
    descripcion: Optional[str] = None
    disponible: bool = False