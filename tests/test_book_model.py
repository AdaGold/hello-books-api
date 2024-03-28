from app.models.book import Book

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Book(id = 1,
                    title="Ocean Book",
                    description="watr 4evr")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["id"] == 1
    assert result["title"] == "Ocean Book"
    assert result["description"] == "watr 4evr"

def test_to_dict_missing_id():
    # Arrange
    test_data = Book(title="Ocean Book",
                    description="watr 4evr")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["id"] is None
    assert result["title"] == "Ocean Book"
    assert result["description"] == "watr 4evr"

def test_to_dict_missing_title():
    # Arrange
    test_data = Book(id=1,
                    description="watr 4evr")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["id"] == 1
    assert result["title"] is None
    assert result["description"] == "watr 4evr"

def test_to_dict_missing_description():
    # Arrange
    test_data = Book(id = 1,
                    title="Ocean Book")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["id"] == 1
    assert result["title"] == "Ocean Book"
    assert result["description"] is None