# schemas/person_schema.py
from pydantic import BaseModel
from datetime import date
from typing import Optional

class PersonBase(BaseModel):
    nombre: str
    apellido: str
    dni_cuit_cuil: str
    fecha_nacimiento: date
    nacionalidad: str
    identidad_genero: str
    etnia: bool
    etnia_nombre: Optional[str]
    estado_civil: str
    personas_a_cargo: int
    tipo_contribuyente: str
    actividad_registrada: str
    telefono: str
    dir_calle: str
    dir_numero: str
    dir_piso: Optional[str]
    dir_letra_nro_depto: Optional[str]
    dir_cp: str
    dir_localidad: str
    dir_departamento: str
    dir_provincia: str
    dir_pais: str

class PersonCreate(PersonBase):
    pass

class PersonOut(PersonBase):
    id: int
    user_email: str

    class Config:
        from_attributes = True
