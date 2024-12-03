from sqlalchemy import Column, String, Integer, Date, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY
from src.db.database import Base

class AudiovisualWork(Base):
    __tablename__ = "audiovisual_works"

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, ForeignKey("users.email"), nullable=False)  # Relación con el usuario
    rol = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    formato = Column(String, nullable=False)
    formato_descripcion = Column(String, nullable=True)
    tipo_produccion = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    genero_descripcion = Column(String, nullable=True)
    clasificacion = Column(String, nullable=False)
    lugar = Column(String, nullable=False)
    duracion_minutos = Column(Integer, nullable=False)
    idioma_original = Column(String, nullable=False)
    subtitulos_idioma = Column(String, nullable=True)
    doblaje_idioma = Column(String, nullable=True)
    capitulo_numero = Column(Integer, default=1)
    capitulo_duracion = Column(Integer, default=0)
    resolucion_video = Column(String, default="1920x1080Px", nullable=True)
    audio_tipo = Column(String, default="5.1 - 7.1 Stereo", nullable=True)
    estreno_fecha = Column(Date, nullable=True)
    sinopsis = Column(String, nullable=True)
    storyline = Column(String, nullable=True)
    avant_premier = Column(String, nullable=True)
    avant_premier_iaavim = Column(Boolean, default=False)
    exhibicion = Column(String, nullable=True)
    valoracion_agam = Column(Integer, nullable=True)
    fondos_propios = Column(String, nullable=True)
    asociados_nacionales = Column(String, nullable=True)
    asociados_internacionales = Column(String, nullable=True)
    fondos_iaavim = Column(String, nullable=True)
    fondos_inca = Column(String, nullable=True)
    fondos_gubernamental = Column(String, nullable=True)
    fondos_internacionales = Column(String, nullable=True)
    venta_nacional = Column(String, nullable=True)
    venta_internacional = Column(String, nullable=True)

    # Relación con el usuario
    user_email = Column(String, ForeignKey("users.email"))
    user = relationship("User", back_populates="audiovisual_works")
