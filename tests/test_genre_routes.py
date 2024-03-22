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