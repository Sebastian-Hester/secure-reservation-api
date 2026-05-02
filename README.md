[![CI](https://github.com/Sebastian-Hester/secure-reservation-api/actions/workflows/ci.yml/badge.svg)](https://github.com/Sebastian-Hester/secure-reservation-api/actions/workflows/ci.yml)

# Secure Reservation API

FastAPI + SQLite backend demonstrating secure authentication, role-based access control, and protected data operations.

## Features
- Health endpoint (`GET /health`)
- User registration with secure password hashing (Argon2)
- JWT login (`POST /auth/login`)
- Protected user endpoint (`GET /me`)
- Authenticated reservations:
  - Create reservation (`POST /reservations`)
  - List your reservations (`GET /reservations`)

## Security Features

- Password hashing using Argon2
- JWT-based authentication and session management
- Protected endpoints requiring valid tokens
- Input validation using pydantic models
- Separation of user data and access control

## 📊 Secure Reservation System – Analytics Dashboard

This project extends a secure FastAPI backend into an analytics workflow by exporting operational metrics and visualizing them in Tableau.

**Live Dashboard:**  
https://public.tableau.com/views/SecureReservationSystem-OperationalMetrics/SecureReservationSystem-OperationalMetrics

### What This Demonstrates
- End-to-end data flow from API → database → analytics → dashboard
- SQL-driven aggregation of operational metrics
- Data visualization for business decision-making
- Secure backend design paired with analytics insights

### Key Metrics Visualized
- Total reservations created
- Daily reservation volume trends
- Average party size trends over time
- Reservations by day of week

### Tech Stack
- FastAPI (Python)
- SQLAlchemy + SQLite
- Alembic migrations
- SQL aggregations
- Tableau Public (dashboard & storytelling)


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

## Example Usage

### Register a User
POST /auth/register

```json
{
  "email": "test@example.com",
  "password": "securepassword"
}
```

## Future Improvements

- Role-based authorization (admin vs user)
- Rate limiting to prevent abuse
- Docker containerization
- Deployment to cloud (AWS/Azure)

# Projects

## 📊 Tableau + Additional Information

This project extends a secure FastAPI backend into an analytics workflow by exporting operational metrics and visualizing them in Tableau.

**Live Tableau Dashboard:**  
https://public.tableau.com/views/SecureReservationSystem-OperationalMetrics/SecureReservationSystem-OperationalMetrics

### What This Demonstrates
- End-to-end data flow from API → database → analytics → dashboard
- SQL-driven aggregation of operational metrics
- Secure backend design paired with business intelligence insights

### Key Metrics Visualized
- Total reservations created
- Daily reservation volume trends
- Average party size trends over time
- Reservations by day of week

### Tech Stack
- FastAPI (Python)
- SQLAlchemy + SQLite
- Alembic migrations
- SQL aggregations
- Tableau Public






