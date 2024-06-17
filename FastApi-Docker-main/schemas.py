from pydantic import BaseModel
from datetime import date

# Schéma de base pour un film
class MovieBase(BaseModel):
    title: str
    director: str
    release_date: date
    genre: str
    duration: int

# Schéma pour créer un nouveau film
class MovieCreate(MovieBase):
    pass

# Schéma pour retourner les détails d'un film
class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True
