#/schemas/audiovisual_upload_schema.py
from pydantic import BaseModel
from typing import Optional

class AudiovisualUploadBase(BaseModel):
    descripcion: str

class AudiovisualUploadCreate(AudiovisualUploadBase):
    audiovisual_work_id: int

class AudiovisualUploadOut(AudiovisualUploadBase):
    id: int
    pdf_path: Optional[str]

    class Config:
        from_attributes = True
