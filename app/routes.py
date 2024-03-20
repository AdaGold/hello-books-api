from flask import Blueprint, abort, make_response, request, Response
from app.models.book import Book
from .db import db

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.post("")
def create_book():
    request_body = request.get_json()
    title = request_body.get("title")
    description = request_body.get("description")

    new_book = Book(title=title, description=description)
    db.session.add(new_book)
    db.session.commit()

    return make_response(new_book.to_dict(), 201)

@books_bp.get("")
def get_all_books():
    query = db.select(Book)

    # If we have a `title` query parameter, we can add on to the query object
    title_param = request.args.get("title")
    if title_param:
        # Match the title_param exactly, including capitalization
        # query = query.where(Book.title == title_param)

        # If we want to allow partial matches, we can use the % wildcard with `like()`
        # If `title_param` contains "Great", the code below will match 
        # both "The Great Gatsby" and "Great Expectations"
        # query = query.where(Book.title.like(f"%{title_param}%"))

        # If we want to allow searching case-insensitively, 
        # we could use ilike instead of like
        query = query.where(Book.title.ilike(f"%{title_param}%"))

    # If we have other query parameters, we can continue adding to the query
    description_param = request.args.get("description")
    if description_param:
        # In case there are books with similar titles, we can also filter by description
        query = query.where(Book.description.ilike(f"%{description_param}%"))

    books = db.session.scalars(query.order_by(Book.id))
    # We could also write the line above as:
    # books = db.session.execute(query).scalars()

    books_response = []
    for book in books:
        books_response.append(book.to_dict())
    return books_response

@books_bp.get("/<book_id>")
def get_one_book(book_id):
    book = validate_book(book_id)

    return book.to_dict()

@books_bp.put("/<book_id>")
def update_book(book_id):
    book = validate_book(book_id)
    request_body = request.get_json()

    book.title = request_body.get("title")
    book.description = request_body.get("description")
    db.session.commit()

    return Response(status=204)

@books_bp.delete("/<book_id>")
def delete_book(book_id):
    book = validate_book(book_id)
    db.session.delete(book)
    db.session.commit()

    return Response(status=204)

def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        response = {"message": f"book {book_id} invalid"}
        abort(make_response(response , 400))

    query = db.select(Book).where(Book.id == book_id)
    book = db.session.scalar(query)

    if not book:
        response = {"message": f"book {book_id} not found"}
        abort(make_response(response, 404))

    return book