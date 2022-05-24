from gettodos import buscar_json_todos_por_id
from posttodos import cadastrar_todos
from posttodos import cadastrar_todos_content
from puttodos import atualizar_completo_todos
from patchtodos import atualizar_parcial_todos
from deletetodos import remover_todos

if __name__ == "__main__":
    buscar_json_todos_por_id(1)
    cadastrar_todos()
    cadastrar_todos_content()
    atualizar_completo_todos()
    atualizar_parcial_todos()
    remover_todos()
