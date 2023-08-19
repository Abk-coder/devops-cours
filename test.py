# tests/test_main.py
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, DIC2!"}


@patch("main.redis_client.incr")
def test_visited_endpoint(mock_incr):
    mock_incr.return_value = 2

    response = client.get("/visited")
    assert response.status_code == 200
    assert response.json() == {"Hello": "DIC2!", "visits": 2}
