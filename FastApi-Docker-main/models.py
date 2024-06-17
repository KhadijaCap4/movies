from sqlalchemy import Column, Integer, String, Date
from database import Base

# Modèle pour la table des films
class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)  # Titre du film
    director = Column(String(255), index=True)  # Réalisateur du film
    release_date = Column(Date)  # Date de sortie du film
    genre = Column(String(50))  # Genre du film
    duration = Column(Integer)  # Durée du film en minutes
