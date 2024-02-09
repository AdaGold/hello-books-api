from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]

    # An instance function that returns a  
    # dictionary which represents the book model
    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            description=self.description
        )
    
    @classmethod
    def from_dict(cls, data):
        try:
            title = data['title']
            description = data['description']
            return cls(title=title, description=description)
        except KeyError as e:
            raise ValueError(f"Missing required field: {e}")