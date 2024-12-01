from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.models.training_model import Training
from src.models.user_model import User
from src.schemas.training_schema import TrainingCreate, TrainingOut
from src.auth.permissions import has_role
import os
from uuid import uuid4

TRAINING_UPLOAD_DIR = "uploads/"

training_router = APIRouter()

# Crear un nuevo training
@training_router.post("/", response_model=TrainingOut)
def create_training(
    training: TrainingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(has_role(["admin", "editor"]))
):
    new_training = Training(**training.dict(), user_email=current_user.email)
    db.add(new_training)
    db.commit()
    db.refresh(new_training)
    return new_training

# Listar trainings asociados al usuario autenticado
@training_router.get("/", response_model=list[TrainingOut])
def list_trainings(
    db: Session = Depends(get_db),
    current_user: User = Depends(has_role(["admin", "editor"]))
):
    if has_role(["admin"]):
        training = db.query(Training).filter().all()
    else:
        training = db.query(Training).filter(Training.user_email == current_user.email).all()
    return training

# Subir un archivo PDF para un training
@training_router.post("/{training_id}/upload", response_model=TrainingOut)
def upload_pdf(
    training_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(has_role(["admin", "editor"]))
):
    training = db.query(Training).filter(
        Training.id == training_id, Training.user_email == current_user.email
    ).first()

    if not training:
        raise HTTPException(status_code=404, detail="Training no encontrado")

    if not training.curso_completo:
        raise HTTPException(status_code=400, detail="Solo puedes subir archivos a cursos completos")

    # Validar tipo de archivo
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Solo se permiten archivos PDF")

    # Guardar el archivo con un nombre único
    file_id = str(uuid4())
    file_path = os.path.join(TRAINING_UPLOAD_DIR, f"{file_id}.pdf")
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    # Asociar el archivo al training
    training.pdf_path = file_path
    db.commit()
    db.refresh(training)
    return training

# Obtener detalles de un training por ID
@training_router.get("/{training_id}", response_model=TrainingOut)
def get_training(
    training_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(has_role(["admin", "editor", "viewer"]))
):
    training = db.query(Training).filter(
        Training.id == training_id, Training.user_email == current_user.email
    ).first()
    if not training:
        raise HTTPException(status_code=404, detail="Training no encontrado")
    return training

# Eliminar un training
@training_router.delete("/{training_id}")
def delete_training(
    training_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(has_role(["admin", "editor"]))
):
    if has_role(["admin"]):
        training = db.query(Training).filter(Training.id == training_id).first()
    else:
        training = db.query(Training).filter(
            Training.id == training_id, Training.user_email == current_user.email
        ).first()

    if not training:
        raise HTTPException(status_code=404, detail="Training no encontrado")

    # Eliminar el archivo asociado si existe
    if training.pdf_path and os.path.exists(training.pdf_path):
        os.remove(training.pdf_path)

    db.delete(training)
    db.commit()
    return {"message": "Training eliminado correctamente"}
