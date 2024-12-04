# models/collaborator_model.py
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.db.database import Base

class Collaborator(Base):
    __tablename__ = "collaborators"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    dni_cuil = Column(String, unique=True, nullable=False)
    role_description = Column(String, nullable=False)
    audiovisual_work_id = Column(Integer, ForeignKey("audiovisual_works.id"))

    audiovisual_work = relationship("AudiovisualWork", back_populates="collaborators")
