import json
import requests


def buscar_dados():
    request = requests.get("http://localhost:3002/api/todo")
    todos = json.loads(request.content)
    print(todos)
    print(todos[0]['titulo'])


def buscar_dados_por_id(id):
    request = requests.get(f'http://localhost:3002/api/todo?id={id}')
    todo = json.loads(request.content)
    print(todo)
    print(todo['titulo'])
