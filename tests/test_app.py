import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    res = client.get("/")
    assert res.status_code == 200


def test_add_todo(client):
    res = client.post("/add", json={"title": "Test Task"})
    assert res.status_code == 200
    assert res.get_json()["success"] == True


def test_add_empty_todo(client):
    res = client.post("/add", json={"title": ""})
    assert res.status_code == 400
