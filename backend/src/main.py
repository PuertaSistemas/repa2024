from fastapi import FastAPI
from src.routes.user_routes import user_router
from src.routes.person_routes import person_router
from src.routes.company_routes import company_router
from src.routes.training_routes import training_router
from src.routes.collaborator_routes import collaborator_router
from src.routes.audiovisual_work_routes import audiovisual_router
from src.db.database import Base, engine

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.title = "REPA IAViM - 2024"
app.version = "0.0.1"

# Incluir rutas
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(person_router, prefix="/persons", tags=["Persons"])
app.include_router(training_router, prefix="/training", tags=["Training"])
app.include_router(company_router, prefix="/company", tags=["Company"])
app.include_router(audiovisual_router, prefix="/audiovisual-works", tags=["Audiovisual Works"])
app.include_router(collaborator_router, prefix="/collaborators", tags=["Collaborators"])

@app.get("/")
def root():
    return {"message": "API de Gestión de Usuarios funcionando correctamente"}
