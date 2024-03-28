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