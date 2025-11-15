import os
import sys
import json

# 👇 Add the project root (one level above /tests) to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app



def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"


def test_get_items():
    client = app.test_client()
    response = client.get("/items")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)


def test_create_item():
    client = app.test_client()
    payload = {"name": "Water"}
    response = client.post(
        "/items",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Water"
    assert "id" in data
