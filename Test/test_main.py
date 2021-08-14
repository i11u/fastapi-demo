from fastapi.testclient import TestClient

from Main.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello, World!"}

def test_read_main2():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World!"} 