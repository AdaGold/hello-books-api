from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship("Author", back_populates="books")
    genres = db.relationship("Genre", secondary="book_genre", backref="books")

    def to_dict(self):
        book_dict = {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }
        if self.author:
            book_dict["author"] = self.author.name

        if self.genres:
            genre_names = [genre.name for genre in self.genres]
            book_dict["genres"] = genre_names

        return book_dict

    @classmethod
    def from_dict(cls, book_data):
        new_book = Book(title=book_data["title"],
                        description=book_data["description"])
        return new_book