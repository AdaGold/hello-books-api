from app.routes.route_utilities import validate_model
from app.models.book import Book
from werkzeug.exceptions import HTTPException
import pytest

def test_validate_model(two_saved_books):
    # Act
    result_book = validate_model(Book, 1)

    # Assert
    assert result_book.id == 1
    assert result_book.title == "Ocean Book"
    assert result_book.description == "watr 4evr"

def test_validate_model_missing_record(client, two_saved_books):
    # Act & Assert
    # Calling `validate_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException) as error:
        result_book = validate_model(Book, "3")

    response = error.value.response
    assert response.status == "404 NOT FOUND"
    
def test_validate_model_invalid_id(two_saved_books):
    # Act & Assert
    # Calling `validate_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException) as error:
        result_book = validate_model(Book, "cat")

        response = error.value.response
        assert response.status == "400 BAD REQUEST"