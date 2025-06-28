# 📌 To-Do API com FastAPI e TDD

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Pytest](https://img.shields.io/badge/Pytest-8.4.1-green?style=for-the-badge)

Uma API minimalista para gerenciar tarefas, desenvolvida com **FastAPI** seguindo **TDD** (Test-Driven Development).

## 🚀 Estrutura do Projeto
todo-fastapi/
├── main.py # Implementação principal da API
├── test_todo_app.py # Testes automatizados
└── requirements.txt # Dependências

text

## 🔧 Funcionalidades Implementadas

### Endpoints
| Método | Rota       | Descrição                          | Body Esperado                     |
|--------|------------|------------------------------------|-----------------------------------|
| `GET`  | `/`        | Verifica status da API             | -                                 |
| `POST` | `/todos/`  | Cria uma nova tarefa               | `{"title": "string", "description": "string"}` |
| `GET`  | `/todos/`  | Lista todas as tarefas cadastradas | -                                 |

### Testes Automatizados (TDD)
- ✅ `test_read_root`: Verifica o endpoint raiz
- ✅ `test_create_todo`: Testa criação de tarefas
- ✅ `test_read_todos`: Verifica listagem de tarefas

## 🛠 Como Executar

### Pré-requisitos
- Python 3.11+
- Pip

### Instalação
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/todo-fastapi.git
cd todo-fastapi

# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.\.venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt
Executando a API
bash
uvicorn main:app --reload
Acesse a documentação interativa:
🔗 http://127.0.0.1:8000/docs
🔗 http://127.0.0.1:8000/redoc

Rodando os Testes
bash
pytest test_todo_app.py -v
📝 Exemplos de Uso
Criando uma tarefa
bash
curl -X POST "http://localhost:8000/todos/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Estudar FastAPI", "description": "Praticar TDD"}'
Listando tarefas
bash
curl "http://localhost:8000/todos/"
💻 Tecnologias Utilizadas
FastAPI - Framework web moderno

Pydantic - Validação de dados

Pytest - Framework de testes

HTTPX - Cliente HTTP para testes

📌 Próximos Passos (To-Do)
Adicionar DELETE endpoint

Implementar banco de dados SQLite

Adicionar autenticação JWT

🤝 Como Contribuir
Faça um fork do projeto

Crie uma branch (git checkout -b feature/nova-funcionalidade)

Commit suas mudanças (git commit -m 'Adiciona nova feature')

Push para a branch (git push origin feature/nova-funcionalidade)

Abra um Pull Request
