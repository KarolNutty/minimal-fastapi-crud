import pytest
from fastapi.testclient import TestClient
from main import app
from pydantic import ValidationError


@pytest.fixture
def client():
    return TestClient(app)


# Teste 1: Rota raiz (GET /)
def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Vamos de TDD!"}


# Teste 2: Criação de TODO (POST /todos/)
def test_create_todo(client):
    # Setup
    test_data = {"title": "Teste TDD", "description": "Criando um item"}

    # Execução
    response = client.post("/todos/", json=test_data)

    # Verificações
    assert response.status_code == 200
    assert response.json()["title"] == test_data["title"]
    assert "id" in response.json()


# Teste 3: Validação de dados (POST inválido)
def test_create_todo_invalid(client):
    with pytest.raises(ValidationError):
        client.post("/todos/", json={"description": "Sem título!"})


# Teste 4: Listagem de TODOs (GET /todos/)
def test_read_todos(client):
    # Primeiro cria um item
    client.post("/todos/", json={"title": "Item para listar"})

    # Depois testa a listagem
    response = client.get("/todos/")
    assert response.status_code == 200
    assert len(response.json()["todos"]) > 0


# Teste 5: Exclusão de TODO (escreva antes de implementar)
def test_delete_todo(client):
    # Cria um item primeiro
    create_res = client.post("/todos/", json={"title": "Para deletar"})
    todo_id = create_res.json()["id"]

    # Deleta
    delete_res = client.delete(f"/todos/{todo_id}")
    assert delete_res.status_code == 200

    # Verifica se foi removido
    list_res = client.get("/todos/")
    assert todo_id not in [t["id"] for t in list_res.json()["todos"]]