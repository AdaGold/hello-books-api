from flask import Flask
from .db import db, migrate
from .models import book
from .routes.book_routes import bp as books_bp
import os

def create_app(test_config=None):
    app = Flask(__name__)

    if not test_config:
        database_uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else:
        app.config["TESTING"] = True
        database_uri = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(books_bp)

    return app