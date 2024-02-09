
from flask import Blueprint, jsonify, abort, make_response
from ..db import db
from ..model.book import Book

# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Fictional Book", "A fantasy novel set in an imaginary world."),
#     Book(2, "Wheel of Time", "A fantasy novel set in an imaginary world."),
#     Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
# ]

bp = Blueprint("books", __name__, url_prefix="/books")

# You may see uses of Model.query to build queries.
# This is an older interface for queries that is considered legacy
# in SQLAlchemy. Prefer using db.session.execute(db.select(...)) instead.
# db.select resource: https://docs.sqlalchemy.org/en/20/tutorial/data_select.html

@bp.get("/")
def index():
    models = db.session.execute(db.select(Book).order_by(Book.id)).scalars()

    return list(map(Book.to_dict, models))

@bp.get("/<id>")
def get(id):
    model = db.session.execute(db.select(Book).filter_by(id=id)).scalar()
    if not model:
        abort(make_response(dict(detail=f"invalid id {id}"), 404))

    return model.to_dict()

#def validate_book(book_id):
#    try:
#        book_id = int(book_id)
#    except:
#        abort(make_response({"message":f"book {book_id} invalid"}, 400))
#
#    for book in books:
#        if book.id == book_id:
#            return book
#
#    abort(make_response({"message":f"book {book_id} not found"}, 404))
        

# @books_bp.route("", methods=["GET"])
# def handle_books():
#     books_response = []
#     for book in books:
#         books_response.append(
#             {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }
#         )
#     return jsonify(books_response)

# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = validate_book(book_id)
#
#     return {
#           "id": book.id,
#           "title": book.title,
#           "description": book.description,
#     }
