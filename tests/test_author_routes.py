def test_create_one_author(client):
    # Act
    response = client.post("/authors", json={
        "name": "New Author"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New Author"
    }

def test_create_one_author_no_name(client):
    # Arrange
    test_data = {}

    # Act
    response = client.post("/authors", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing name'}

def test_create_one_author_with_extra_keys(client):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "name": "New Author",
        "another": "last value"
    }

    # Act
    response = client.post("/authors", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New Author"
    }

def test_get_all_authors_one_saved_author(client, one_saved_author):
    # Act
    response = client.get("/authors")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 1,
        "name": "New Author 1",
    }

def test_get_all_authors_no_saved_author(client):
    # Act
    response = client.get("/authors")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []    

def test_create_book_with_author(client, one_saved_author):
    # Arrange
    test_data = {
        "title": "New Book",
        "description": "The Best!"
    }

    # Act
    response = client.post("/authors/1/books", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "title": "New Book",
        "description": "The Best!",
        "author": "New Author 1"
    }

def test_create_book_with_nonexistant_author(client):
    # Arrange
    test_data = {
        "title": "New Book",
        "description": "The Best!"
    }

    # Act
    response = client.post("/authors/1/books", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message":"Author 1 not found"}

def test_create_book_with_bad_author_id(client):
    # Arrange
    test_data = {
        "title": "New Book",
        "description": "The Best!"
    }

    # Act
    response = client.post("/authors/cat/books", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message":"Author cat invalid"}

def test_get_books_by_author_expects_two_books(client, two_saved_books, author_with_two_books):
    # Act
    response = client.get("/authors/1/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body == [
        {
            "id": 3,
            "title": "Desert Book",
            "description": "Sands all around",
            "author": "New Author 1"
        },
        {
            "id": 4,
            "title": "Plains Book",
            "description": "Grasslands for miles",
            "author": "New Author 1"
        }
    ]

def test_get_books_by_author_with_no_books(client, two_saved_books, one_saved_author):
    # Act
    response = client.get("/authors/1/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 0
    assert response_body == []    