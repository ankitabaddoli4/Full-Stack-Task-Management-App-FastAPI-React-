from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={
        "title": "Test Task",
        "description": "Testing"
    })
    assert response.status_code == 200

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200