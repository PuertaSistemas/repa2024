from sqlalchemy import Column, String, Date, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base

class Training(Base):
    __tablename__ = "trainings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    institucion = Column(String, nullable=False)
    curso = Column(String, nullable=False)
    ano_inicio = Column(Date, nullable=False)
    dictado_iaavim = Column(Boolean, default=False)
    curso_completo = Column(Boolean, default=False)
    ano_finalizado = Column(Date, nullable=True)
    pdf_path = Column(String, nullable=True)  # Ruta del archivo PDF

    user_email = Column(String, ForeignKey("users.email"))
    user = relationship("User", back_populates="trainings")
