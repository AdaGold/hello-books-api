def test_create_one_genre(client):
    # Act
    response = client.post("/genres", json={
        "name": "New Genre"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New Genre"
    }

def test_create_one_genre_no_name(client):
    # Arrange
    test_data = {}

    # Act
    response = client.post("/genres", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing name'}

def test_create_one_genre_with_extra_keys(client):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "name": "New Genre",
        "another": "last value"
    }

    # Act
    response = client.post("/genres", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New Genre"
    }

def test_create_book_with_genre(client, one_saved_genre):
    # Arrange
    test_data = {
        "title": "New Book",
        "description": "The Best!"
    }

    # Act
    response = client.post("/genres/1/books", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "title": "New Book",
        "description": "The Best!",
        "genres": ["New Genre 1"]
    }

def test_create_book_with_nonexistant_genre(client):
    # Arrange
    test_data = {
        "title": "New Book",
        "description": "The Best!"
    }

    # Act
    response = client.post("/genres/1/books", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message":"Genre 1 not found"}

def test_create_book_with_bad_genre_id(client):
    # Arrange
    test_data = {
        "title": "New Book",
        "description": "The Best!"
    }

    # Act
    response = client.post("/genres/cat/books", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message":"Genre cat invalid"}

def test_get_books_by_genre_expects_two_books(client, two_saved_books, genre_with_two_books):
    # Act
    response = client.get("/genres/1/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body == [
        {
            "id": 3,
            "title": "Sky Book",
            "description": "Floating in the clouds",
            "genres": ["New Genre 1"]
        },
        {
            "id": 4,
            "title": "Tundra Book",
            "description": "Like plains but colder",
            "genres": ["New Genre 1"]
        }
    ]

def test_get_books_by_genre_with_no_books(client, two_saved_books, one_saved_genre):
    # Act
    response = client.get("/genres/1/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 0
    assert response_body == []