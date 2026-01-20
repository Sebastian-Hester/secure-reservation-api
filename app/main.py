from fastapi import FastAPI
from .db import engine
from .models import Base

app = FastAPI(title="Secure Reservation API", version="0.2.0")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}
