from app.models.genre import Genre
import pytest

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Genre(id = 1, name="New Genre")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 2
    assert result["id"] == 1
    assert result["name"] == "New Genre"

def test_to_dict_missing_id():
    # Arrange
    test_data = Genre(name="New Genre")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 2
    assert result["id"] is None
    assert result["name"] == "New Genre"

def test_to_dict_missing_name():
    # Arrange
    test_data = Genre(id=1)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 2
    assert result["id"] == 1
    assert result["name"] is None

def test_from_dict_returns_genre():
    # Arrange
    genre_data = {"name": "New Genre"}

    # Act
    new_genre = Genre.from_dict(genre_data)

    # Assert
    assert new_genre.name == "New Genre"

def test_from_dict_with_no_name():
    # Arrange
    genre_data = {}

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_book = Genre.from_dict(genre_data)

def test_from_dict_with_extra_keys():
    # Arrange
    genre_data = {
        "extra": "some stuff",
        "name": "New Genre",
        "another": "last value"
    }

    # Act
    new_genre = Genre.from_dict(genre_data)

    # Assert
    assert new_genre.name == "New Genre"