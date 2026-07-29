import requests

def test_get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Leanne Graham"

def test_create_post():
    payload = {"title": "Học API", "body": "Nội dung test", "userId": 1}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "Học API"

def test_update_post():
    payload = {"id": 1, "title": "Đã sửa", "body": "Nội dung mới", "userId": 1}
    response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Đã sửa"

def test_delete_post():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200