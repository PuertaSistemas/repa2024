from pydantic import BaseModel, Field, validator
from typing import Literal, Optional
from datetime import date

class AudiovisualWorkBase(BaseModel):
    rol: str
    estado: Literal["DESARROLLO",
    "PREPRODUCCIÓN",
    "RODAJE - PRODUCCIÓN",
    "POSPRODUCCIÓN",
    "EXHIBICIÓN/FINALIZADA"]
    nombre: str
    formato: Literal["Cortometraje", "Largometraje", "Serie", "Videoclips", "Otros"]
    formato_descripcion: Optional[str]
    tipo_produccion: Literal["Comunitaria", "Independiente", "Industrial"]
    genero: Literal[
        "Ficción",
        "Documental",
        "Animación",
        "Televisivo",
        "Videodanza",
        "Experimental",
        "Otros"]
    genero_descripcion: Optional[str]
    clasificacion: Literal["ATP", "+13", "+16", "+18", "C"]
    lugar: Literal[
        "Misiones",
        "Región",
        "Argentina",
        "Internacional"]
    duracion_minutos: int
    idioma_original: Literal[
        "Español",
        "Inglés",
        "Portugués",
        "Guaraní",
        "Francés",
        "OTRO"]
    subtitulos_idioma: Optional[
        Literal[
            "Español",
            "Inglés",
            "Portugués",
            "Guaraní",
            "Francés",
            "OTRO"]
    ]
    doblaje_idioma: Optional[str]
    capitulo_numero: int = 1
    capitulo_duracion: int = 0
    resolucion_video: str = "1920x1080Px"
    audio_tipo: str = "5.1 - 7.1 Stereo"
    estreno_fecha: date
    sinopsis: str
    storyline: Optional[str]
    avant_premier: Optional[str]
    avant_premier_iaavim: bool = False
    exhibicion: Optional[Literal["VENTANAS TRADICIONALES", "VENTANAS NO TRADICIONALES"]]
    valoracion_agam: Optional[int]
    fondos_propios: Optional[Literal["TOTAL", "PARCIAL"]]
    asociados_nacionales: Optional[Literal["TOTAL", "PARCIAL"]]
    asociados_internacionales: Optional[Literal["TOTAL", "PARCIAL"]]
    fondos_iaavim: Optional[Literal["TOTAL", "PARCIAL"]]
    fondos_inca: Optional[Literal["TOTAL", "PARCIAL"]]
    fondos_gubernamental: Optional[Literal["TOTAL", "PARCIAL"]]
    fondos_internacionales: Optional[Literal["TOTAL", "PARCIAL"]]
    venta_nacional: Optional[Literal["TOTAL", "PARCIAL"]]
    venta_internacional: Optional[Literal["TOTAL", "PARCIAL"]]

    #@validator("formato_descripcion")
    #def validate_format(cls, formato, values):
        # Si "formato" es True, "formato_descripcion" debe ser proporcionado
    #    if values.get("formato") and not formato_descripcion:
    #        raise ValueError("Si el formato es 'Otros', el campo 'formato_descripcion' es obligatorio.")
    #    return formato_descripcion

    #@validator("genero_descripcion")
    #def validate_genero(cls, genero, values):
        # Si "genero" es True, "genero_descripcion" debe ser proporcionado
    #    if values.get("genero") and not genero_descripcion:
    #        raise ValueError("Si el género es 'Otros', el campo 'genero_descripcion' es obligatorio.")
    #    return genero_descripcion

class AudiovisualWorkCreate(AudiovisualWorkBase):
    pass

class AudiovisualWorkOut(AudiovisualWorkBase):
    id: int
    user_email: str

    class Config:
        from_attributes = True
