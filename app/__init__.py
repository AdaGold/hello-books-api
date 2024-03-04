from flask import Flask
from .routes import hello_world_bp


def create_app(test_config=None):
    app = Flask(__name__)

    # Register Blueprints here
    app.register_blueprint(hello_world_bp)

    return app
