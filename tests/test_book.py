import pytest
from app.model.book import Book

def test_to_dict():
    book = Book(title='Test Book', description='This is a test book')
    expected_dict = {
        'id': None,
        'title': 'Test Book',
        'description': 'This is a test book'
    }
    assert book.to_dict() == expected_dict

def test_from_dict():
    data = {
        'title': 'Test Book',
        'description': 'This is a test book'
    }
    book = Book.from_dict(data)
    assert book.title == 'Test Book'
    assert book.description == 'This is a test book'

def test_from_dict_missing_field():
    data = {
        'title': 'Test Book'
    }
    with pytest.raises(ValueError) as e:
        Book.from_dict(data)
