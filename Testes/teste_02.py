import requests
import jsonschema
from jsonschema import validate

def test_schema_validation():
    """Valida estrutura dos dados da API"""
    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title", "body"]
    }

    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    validate(instance=response.json(), schema=schema)
    print("✅ Schema validado com sucesso")

if __name__ == "__main__":
    test_schema_validation()
