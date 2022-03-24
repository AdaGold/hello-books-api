from app import db
from app.models.author import Author
from app.models.book import Book
from app.models.genre import Genre
from flask import Blueprint, jsonify, abort, make_response, request

genres_bp = Blueprint("genres_bp", __name__, url_prefix="/genres")

def validate_genre(genre_id):
    try:
        genre_id = int(genre_id)
    except:
        abort(make_response({"message":f"genre {genre_id} invalid"}, 400))

    genre = Genre.query.get(genre_id)

    if not genre:
        abort(make_response({"message":f"genre {genre_id} not found"}, 404))

    return genre

@genres_bp.route("", methods=["POST"])
def create_genre():
    request_body = request.get_json()
    new_genre = Genre(name=request_body["name"],)

    db.session.add(new_genre)
    db.session.commit()

    return make_response(jsonify(f"Genre {new_genre.name} successfully created"), 201)

@genres_bp.route("", methods=["GET"])
def read_all_genres():
    
    genres = Genre.query.all()

    genres_response = []
    for genre in genres:
        genres_response.append(
            {
                "name": genre.name
            }
        )
    return jsonify(genres_response)

@genres_bp.route("/<genre_id>/books", methods=["POST"])
def create_book(genre_id):

    genre = validate_genre(genre_id)

    request_body = request.get_json()
    new_book = Book(
        title=request_body["title"],
        description=request_body["description"],
        author_id=request_body["author_id"],
        genres=[genre]
    )
    db.session.add(new_book)
    db.session.commit()
    return make_response(jsonify(f"Book {new_book.title} by {new_book.author.name} successfully created"), 201)
