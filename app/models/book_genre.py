from app import db

class BookGenre(db.Model):
    __tablename__ = "book_genre"
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True,nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), primary_key=True,nullable=False)
