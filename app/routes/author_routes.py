from flask import Blueprint, request
from app.models.author import Author
from app.models.book import Book
from .model_utilities import create_model, get_models_with_filters, validate_model

bp = Blueprint("authors_bp", __name__, url_prefix="/authors")

@bp.post("")
def create_author():
    request_body = request.get_json()
    return create_model(Author, request_body)

@bp.get("")
def get_all_authors():
<<<<<<< HEAD
    query = db.select(Author)
    
    name_param = request.args.get("name")
    if name_param:
        query = query.where(Author.name.ilike(f"%{name_param}%"))
    
    authors = db.session.scalars(query.order_by(Author.id))
    authors_response = [author.to_dict() for author in authors]

return authors_response
=======
    filters = request.args
    return get_models_with_filters(Author, filters)
>>>>>>> 97a2318 (Refactor model creation and fetching and filtering models to the model_utilities file)

@bp.post("/<author_id>/books")
def create_book_with_author(author_id):
    author = validate_model(Author, author_id)

    request_body = request.get_json()
    request_body["author_id"] = author.id
    return create_model(Book, request_body)

@bp.get("/<author_id>/books")
def get_books_by_author(author_id):
    author = validate_model(Author, author_id)
    response = [book.to_dict() for book in author.books]
    return response