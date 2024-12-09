from fastapi import FastAPI
from src.routes.user_routes import user_router
from src.routes.person_routes import person_router
from src.routes.company_routes import company_router
from src.routes.training_routes import training_router
from src.routes.collaborator_routes import collaborator_router
from src.routes.audiovisual_work_routes import audiovisual_router
from src.routes.audiovisual_upload_routes import audiovisual_upload_router
from src.db.database import Base, engine

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.title = "REPA IAViM - 2024"
app.version = "0.0.12"

# Incluir rutas a módulos
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(person_router, prefix="/persons", tags=["Persons"]) # Datos Personales
app.include_router(training_router, prefix="/training", tags=["Training"]) # Formación de la Persona Física
app.include_router(company_router, prefix="/company", tags=["Company"]) # Persona Juridica - Compañias Empresas creadas por la Persona

# Audio Visuales realizados por la persona / Empresa
app.include_router(audiovisual_router, prefix="/audiovisual-works", tags=["Audiovisual Works"])
app.include_router(audiovisual_upload_router, prefix="/audiovisual-upload", tags=["Upload Image"])
app.include_router(collaborator_router, prefix="/collaborators", tags=["Collaborators"])
# Participación de Persona Juridica / Empresa en Foros o reuniones
#

@app.get("/")
def root():
    return {"message": "API de Gestión de Usuarios funcionando correctamente"}
