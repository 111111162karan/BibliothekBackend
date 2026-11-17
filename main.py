from contextlib import asynccontextmanager

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy import text

from database import engine
import models
from routers import user


# Tabellen anlegen (falls noch nicht vorhanden)
models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Bibliothek API",
    description="Bibliothek API",
    version="1.0.0",
)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Hello to my World\n Besuche /docs für die Swagger-UI"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
