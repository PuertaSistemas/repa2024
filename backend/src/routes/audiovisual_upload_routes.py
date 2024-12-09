# routes/audiovisual_upload_routes.py
from src.routes import audiovisual_work_routes
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.models.user_model import User
from src.models.audiovisual_upload_model import AudioVisualUpload
from src.schemas.audiovisual_upload_schema import AudiovisualUploadBase, AudiovisualUploadOut, AudiovisualUploadCreate
from src.auth.permissions import has_role
import os
from uuid import uuid4

# from src.models.training_model import Training
# from src.schemas.training_schema import TrainingCreate, TrainingOut

UPLOAD_DIR = "uploads/"

audiovisual_upload_router = APIRouter()

# Subir un archivo PDF para un training
@audiovisual_upload_router.post("/{audiovisual_id}/upload", response_model=AudiovisualUploadOut)
def upload_pdf(
    audiovisual_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(has_role(["admin", "editor"]))
):
    # Si el administrador no usa el email.
    audiovisualwork = db.query(AudiovisualWork).filter(
        AudiovisualWork.id == audiovisual_id, AudiovisualWork.user_email == current_user.email
    ).first()

    if not audiovisualwork:
        raise HTTPException(status_code=404, detail="Produccion Audiovisual no encontrado")

    # Validar tipo de archivo
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Solo se permiten archivos PDF")

    # Guardar el archivo con un nombre único
    file_id = str(uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}.pdf")
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    # Asociar el archivo al training
    audiovisualupload.pdf_path = file_path
    db.commit()
    db.refresh(audiovisualupload)

    return audiovisualupload
