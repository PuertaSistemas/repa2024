from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models.audiovisual_work_model import AudiovisualWork
from src.schemas.audiovisual_work_schema import AudiovisualWorkCreate, AudiovisualWorkOut
from src.db.database import get_db
from src.auth.permissions import has_role

audiovisual_router = APIRouter()

# Crear una nueva obra audiovisual
@audiovisual_router.post("/", response_model=AudiovisualWorkOut)
def create_audiovisual_work(
    work: AudiovisualWorkCreate,
    db: Session = Depends(get_db),
    current_user = Depends(has_role(["admin", "editor"]))  # Permiso requerido
):
    new_work = AudiovisualWork(**work.dict(), user_email=current_user.email)
    db.add(new_work)
    db.commit()
    db.refresh(new_work)
    return new_work

# Obtener todas las obras audiovisuales
@audiovisual_router.get("/", response_model=list[AudiovisualWorkOut])
def list_audiovisual_works(
    db: Session = Depends(get_db),
    current_user = Depends(has_role(["admin", "editor"]))  # Permiso requerido
):
    works = db.query(AudiovisualWork).filter(AudiovisualWork.user_email == current_user.email).all()
    return works

# Obtener una obra audiovisual específica por ID
@audiovisual_router.get("/{work_id}", response_model=AudiovisualWorkOut)
def get_audiovisual_work(
    work_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(has_role(["admin", "editor"]))  # Permiso requerido
):
    work = db.query(AudiovisualWork).filter(
        AudiovisualWork.id == work_id,
        AudiovisualWork.user_email == current_user.email
    ).first()
    if not work:
        raise HTTPException(status_code=404, detail="Obra audiovisual no encontrada")
    return work

# Eliminar una obra audiovisual
@audiovisual_router.delete("/{work_id}")
def delete_audiovisual_work(
    work_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(has_role(["admin", "editor"]))  # Permiso requerido
):
    work = db.query(AudiovisualWork).filter(
        AudiovisualWork.id == work_id,
        AudiovisualWork.user_email == current_user.email
    ).first()
    if not work:
        raise HTTPException(status_code=404, detail="Obra audiovisual no encontrada")
    db.delete(work)
    db.commit()
    return {"message": "Obra audiovisual eliminada correctamente"}
