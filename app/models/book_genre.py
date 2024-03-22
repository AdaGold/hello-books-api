from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db

class BookGenre(db.Model):
    __tablename__ = "book_genre"

    book_id: Mapped[int] = mapped_column(ForeignKey("book.id"), primary_key=True)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"), primary_key=True)