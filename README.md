# Secure Reservation API

FastAPI + SQLite backend showcasing secure authentication and role-safe data access.

## Features
- Health endpoint (`GET /health`)
- User registration with secure password hashing (Argon2)
- JWT login (`POST /auth/login`)
- Protected user endpoint (`GET /me`)
- Authenticated reservations:
  - Create reservation (`POST /reservations`)
  - List your reservations (`GET /reservations`)

## Run locally
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

## Tests
```bash
pytest -q
```






