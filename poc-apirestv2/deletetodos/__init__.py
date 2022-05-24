import requests
from gettodos import buscar_json_todos_por_id


def remover_todos():
    buscar_json_todos_por_id(10)
    api_url = "https://jsonplaceholder.typicode.com/todos/10"
    response = requests.delete(api_url)
    print(response.json())
    print(response.status_code)
    print()
