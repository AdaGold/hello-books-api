from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    
    @classmethod
    def from_dict(cls, book_data):
        new_book = cls(title=book_data["title"],
                       description=book_data["description"])
        # We could also use `Book` in place of the `cls` keyword  
        # The following declaration is equivalent to the one above
        # new_book = Book(title=book_data["title"],
        #                 description=book_data["description"])

        return new_book