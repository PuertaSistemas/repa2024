from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from pydantic import BaseModel, Field, validator
from typing import Optional, List
#from src.routes.movie_router import movie_router
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_USER= os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD= os.getenv("POSTGRES_PASSWORD")
POSTGRES_PORT= os.getenv("POSTGRES_PORT")
POSTGRES_DB= os.getenv("POSTGRES_DB")

app = FastAPI()
app.title = "REPA IAViM - 2024"
app.version = "0.0.1"

#app.include_router(prefix='/movies', router=movie_router)

@app.get('/', tags=['Home'])
def message():
    secret_key = os.getenv("POSTGRES_DB")
    return {"POSTGRES_USER": POSTGRES_USER, "POSTGRES_PORT": POSTGRES_PORT, "POSTGRES_DB":POSTGRES_DB}
