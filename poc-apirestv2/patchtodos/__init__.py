import requests
from gettodos import buscar_json_todos_por_id


def atualizar_parcial_todos():
    buscar_json_todos_por_id(10)
    api_url = "https://jsonplaceholder.typicode.com/todos/10"
    todo = {"title": "Mow lawn"}
    response = requests.patch(api_url, json=todo)
    print(response.json())
    print(response.status_code)
    print()
