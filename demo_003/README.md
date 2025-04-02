## Steps:
1. Install and verify uv
2. initalize project using `uv init`
3. create virtual env using `uv venv`
4. add fastapi dependency using `uv add "fastapi[standard]"`
5. create basic folder structure
   .
   ├── core
   │ ├── api.py
   │ ├── repository.py
   │ ├── schemas.py
   │ └── service.py
   ├── main.py
   └── pyproject.toml

6. Add basic fastapi server code in main.py and run using `uv run fastapi dev main.py`
