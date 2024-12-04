# schemas/collaborator_schema.py
from pydantic import BaseModel, EmailStr

class CollaboratorBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    dni_cuil: str
    role_description: str

class CollaboratorCreate(CollaboratorBase):
    audiovisual_work_id: int

class CollaboratorOut(CollaboratorBase):
    id: int
    audiovisual_work_id: int

    class Config:
        from_attributes = True
