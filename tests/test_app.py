from http import HTTPStatus


def test_root_return_olamundo(client):
    # Esset teste tem 3 etapas (AAA)
    # A: Arrnge - Arranjo
    # A: Act    - Executa a coisa (SUT)
    # A: Assert - Garanta que A é A

    # arrange
    # client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Olá mundo!'}


def teste_create_users(client):
    response = client.post(
        '/users/',
        json={
            'usuario': 'bob',
            'email': 'bob@example.com',
            'senha': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'bob@example.com',
        'usuario': 'bob',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'email': 'bob@example.com',
                'usuario': 'bob',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'usuario': 'alice',
            'email': 'alice@example.com',
            'senha': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'usuario': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_delet_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'usuario': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }