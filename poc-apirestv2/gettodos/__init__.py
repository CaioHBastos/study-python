import requests


def buscar_json_todos_por_id(id):
    api_url = f"https://jsonplaceholder.typicode.com/todos/{id}"
    response = requests.get(api_url)
    print(response.json())
    print(response.status_code)
    print(response.headers["Content-Type"])
    print()