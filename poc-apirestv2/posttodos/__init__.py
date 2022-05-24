import json

import requests

def cadastrar_todos():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    todo = {"userId": 1, "title": "Buy milk", "completed": False}
    response = requests.post(api_url, json=todo)
    print(response.json())
    print(response.status_code)
    print()

def cadastrar_todos_content():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    todo = {"userId": 2, "title": "Buy beer", "completed": True}
    headers = {"Content-Type": "application/json"}
    response = requests.post(api_url, data=json.dumps(todo), headers=headers)
    print(response.json())
    print(response.status_code)
    print()
