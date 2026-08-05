from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_return_olamundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Olá mundo!'}
