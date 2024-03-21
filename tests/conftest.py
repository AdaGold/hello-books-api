import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from app.models.book import Book
from app.models.author import Author
from app.models.genre import Genre


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_saved_books(app):
    # Arrange
    ocean_book = Book(title="Ocean Book",
                      description="watr 4evr")
    mountain_book = Book(title="Mountain Book",
                         description="i luv 2 climb rocks")

    db.session.add_all([ocean_book, mountain_book])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()


@pytest.fixture
def one_saved_author(app):
    author = Author(name="New Author 1")
    db.session.add(author)
    db.session.commit()


@pytest.fixture
def author_with_two_books(app, one_saved_author):    
    desert_book = Book(title="Desert Book",
                       description="Sands all around",
                       author_id=1)
    plains_book = Book(title="Plains Book",
                       description="Grasslands for miles",
                       author_id=1)

    db.session.add_all([desert_book, plains_book])
    db.session.commit()


@pytest.fixture
def one_saved_genre(app):
    genre = Genre(name="New Genre 1")
    db.session.add(genre)
    db.session.commit()

    return genre


@pytest.fixture
def genre_with_two_books(app, one_saved_genre):   
    sky_book = Book(title="Sky Book",
                       description="Floating in the clouds",
                       genres=[one_saved_genre])
    tundra_book = Book(title="Tundra Book",
                       description="Like plains but colder",
                       genres=[one_saved_genre])

    db.session.add_all([sky_book, tundra_book])
    db.session.commit()