from flask import Blueprint, jsonify, abort, make_response, request
from app.models.book import Book
from sqlalchemy import select
from .db import db

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.post("/")
def create_book():
    request_body = request.get_json()
    title = request_body.get("title")
    description = request_body.get("description")

    new_book = Book(title=title, description=description)
    db.session.add(new_book)
    db.session.commit()

    response = {
        "id": new_book.id,
        "title": new_book.title,
        "description": new_book.description,
    }
    return make_response(response, 201)

@books_bp.get("/")
def get_all_books():
    query = db.select(Book).order_by(Book.id)
    books = db.session.scalars(query)
    # We could also write the line above as:
    # books = db.session.execute(query).scalars()

    books_response = []
    for book in books:
        books_response.append(
            {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        )
    return jsonify(books_response)

@books_bp.get("/<book_id>")
def get_one_book(book_id):
    book = validate_book(book_id)

    return {
        "id": book.id,
        "title": book.title,
        "description": book.description,
    }

@books_bp.put("/<book_id>")
def update_book(book_id):
    book = validate_book(book_id)
    request_body = request.get_json()

    book.title = request_body.get("title")
    book.description = request_body.get("description")
    db.session.commit()

    return {
        "id": book.id,
        "title": book.title,
        "description": book.description,
    }

def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        response = {"message": f"book {book_id} invalid"}
        abort(make_response(response , 400))

    query = db.select(Book).where(Book.id == book_id)
    book = db.session.scalar(query)
    if book:
        return book

    response = {"message": f"book {book_id} not found"}
    abort(make_response(response, 404))

