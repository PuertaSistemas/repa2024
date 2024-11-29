from fastapi import FastAPI
from src.routes.user_routes import user_router
from src.routes.person_routes import person_router
from src.db.database import Base, engine

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.title = "REPA IAViM - 2024"
app.version = "0.0.1"

# Incluir rutas
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(person_router, prefix="/persons", tags=["Persons"])

@app.get("/")
def root():
    return {"message": "API de Gestión de Usuarios funcionando correctamente"}
