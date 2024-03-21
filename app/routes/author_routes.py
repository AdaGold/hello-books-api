from flask import Blueprint, request
from app.models.author import Author
from .model_utilities import create_model, get_models_with_filters

bp = Blueprint("authors_bp", __name__, url_prefix="/authors")

@bp.post("")
def create_author():
    request_body = request.get_json()
    return create_model(Author, request_body)

@bp.get("")
def get_all_authors():
    filters = request.args
    return get_models_with_filters(Author, filters)