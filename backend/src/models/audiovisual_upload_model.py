#/models/audiovisual_upload_model.py
from sqlalchemy import Column, String, Date, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base

class AudioVisualUpload(Base):
    __tablename__ = "audiovisualupload"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    descripcion = Column(String, nullable=False)
    pdf_path = Column(String, nullable=True)  # Ruta del archivo PDF
    audiovisual_work_id = Column(Integer, ForeignKey("audiovisual_works.id"))

    audiovisual_work = relationship("AudiovisualWork", back_populates="audiovisual_uploads")
