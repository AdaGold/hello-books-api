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