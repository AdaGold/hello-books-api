from flask import Flask
from .routes import books_bp

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    # Register Blueprints here
    app.register_blueprint(books_bp)

    return app
