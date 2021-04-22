from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    # Import models here
    from app.models.book import Book

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)

    return app
