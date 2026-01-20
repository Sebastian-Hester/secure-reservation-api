from fastapi import FastAPI

app = FastAPI(title="Secure Reservation API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}
