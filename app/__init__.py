from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    # Register Blueprints here
    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)

    return app
