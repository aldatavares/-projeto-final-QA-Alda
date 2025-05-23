import requests

def test_api_endpoints():
    """Teste CRUD completo com API real"""
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    # CREATE
    new_post = {"title": "QA Test", "body": "Testando API", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    post_id = response.json()["id"]
    
    # READ
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    
    # UPDATE
    updated_data = {"title": "QA Test Updated"}
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_data)
    assert response.status_code == 200
    
    # DELETE
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200

if __name__ == "__main__":
    test_api_endpoints()
    print("✅ Todos os testes de API passaram!")
