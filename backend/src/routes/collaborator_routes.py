# routes/collaborator_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.auth.permissions import has_role
from src.db.database import get_db
from src.models.collaborator_model import Collaborator
from src.schemas.collaborator_schema import CollaboratorCreate, CollaboratorOut

collaborator_router = APIRouter()

# Crear un colaborador
@collaborator_router.post("/", response_model=CollaboratorOut)
def create_collaborator(
    collaborator: CollaboratorCreate,
    db: Session = Depends(get_db),
    current_user = Depends(has_role(["admin", "editor"]))
):
    db_collaborator = db.query(Collaborator).filter(Collaborator.email == collaborator.email).first()
    if db_collaborator:
        raise HTTPException(status_code=400, detail="El colaborador ya existe")

    new_collaborator = Collaborator(**collaborator.dict())
    db.add(new_collaborator)
    db.commit()
    db.refresh(new_collaborator)
    return new_collaborator

# Obtener todos los colaboradores
@collaborator_router.get("/", response_model=list[CollaboratorOut])
def get_collaborators(
    db: Session = Depends(get_db),
    current_user = Depends(has_role(["admin", "editor"]))
):
    return db.query(Collaborator).all()

# Obtener un colaborador por ID
@collaborator_router.get("/{collaborator_id}", response_model=CollaboratorOut)
def get_collaborator(
    collaborator_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(has_role(["admin", "editor"]))
):
    collaborator = db.query(Collaborator).filter(Collaborator.id == collaborator_id).first()
    if not collaborator:
        raise HTTPException(status_code=404, detail="Colaborador no encontrado")
    return collaborator

# Actualizar un colaborador
@collaborator_router.put("/{collaborator_id}", response_model=CollaboratorOut)
def update_collaborator(
    collaborator_id: int,
    updated_data: CollaboratorCreate,
    db: Session = Depends(get_db),
    current_user = Depends(has_role(["admin", "editor"]))
):
    collaborator = db.query(Collaborator).filter(Collaborator.id == collaborator_id).first()
    if not collaborator:
        raise HTTPException(status_code=404, detail="Colaborador no encontrado")

    for key, value in updated_data.dict().items():
        setattr(collaborator, key, value)

    db.commit()
    db.refresh(collaborator)
    return collaborator

# Eliminar un colaborador
@collaborator_router.delete("/{collaborator_id}")
def delete_collaborator(
    collaborator_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(has_role(["admin", "editor"]))
):
    collaborator = db.query(Collaborator).filter(Collaborator.id == collaborator_id).first()
    if not collaborator:
        raise HTTPException(status_code=404, detail="Colaborador no encontrado")

    db.delete(collaborator)
    db.commit()
    return {"message": "Colaborador eliminado correctamente"}
