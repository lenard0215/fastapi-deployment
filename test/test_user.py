from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    res =client.get("/")
    print (res.json().get('message'))

def test_create_user():
    res = client.post("/users/", json={"email":"hello123@gmail.com",
                                       "password": "password1234"})
    
    print(res.json())
    assert res.status_code == 201
    
