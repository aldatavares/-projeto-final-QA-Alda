import requests
import time

def test_api_performance():
    """Testa tempo de resposta da API"""
    start_time = time.time()
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response_time = time.time() - start_time
    
    assert response.status_code == 200
    assert response_time < 1.0
    print(f"✅ Performance OK - Tempo: {response_time:.3f}s")

if __name__ == "__main__":
    test_api_performance()
