import pytest
from fastapi.testclient import TestClient

from fastapi_zero.app import app


# novo arrange de forma mai simples
@pytest.fixture
def client():
    return TestClient(app)
