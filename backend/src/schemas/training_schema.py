from pydantic import BaseModel
from datetime import date
from typing import Optional

class TrainingBase(BaseModel):
    institucion: str
    curso: str
    ano_inicio: date
    dictado_iaavim: bool = False
    curso_completo: bool = False
    ano_finalizado: Optional[date]

class TrainingCreate(TrainingBase):
    pass

class TrainingOut(TrainingBase):
    id: int
    pdf_path: Optional[str]

    class Config:
        from_attributes = True
