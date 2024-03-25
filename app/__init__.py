from flask import Flask
from .routes.book_routes import books_bp

def create_app():
    app = Flask(__name__)

    # Register Blueprints here
    app.register_blueprint(books_bp)

    return app