from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List
from ..db import db

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"), nullable=True)
    author: Mapped["Author"] = relationship(back_populates="books")
    genres: Mapped[List["Genre"]] = relationship(secondary="book_genre", back_populates="books")

    def to_dict(self):
        book_as_dict = {}
        book_as_dict["id"] = self.id
        book_as_dict["title"] = self.title
        book_as_dict["description"] = self.description

        if self.author:
            book_as_dict["author"] = self.author.name

        if self.genres:
            book_as_dict["genres"] = [genre.name for genre in self.genres]

        return book_as_dict
    
    @classmethod
    def from_dict(cls, book_data):
        # Use get() to fetch values that could be undefined to avoid raising an error
        author_id = book_data.get("author_id")
        genres = book_data.get("genres", [])

        new_book = Book(
            title=book_data["title"],
            description=book_data["description"],
            author_id=author_id,
            genres=genres
        )

        return new_book