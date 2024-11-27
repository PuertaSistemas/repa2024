from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from src.routes.user_router import user_router

app = FastAPI()
app.title = "REPA IAViM - 2024"
app.version = "0.0.1"

app.include_router(prefix='/users', router=user_router)

@app.get('/', tags=['Home'])
def message():
    #secret_key = os.getenv("POSTGRES_DB")
    return {"POSTGRES_USER": POSTGRES_USER, "POSTGRES_PORT": POSTGRES_PORT, "POSTGRES_DB":POSTGRES_DB}
