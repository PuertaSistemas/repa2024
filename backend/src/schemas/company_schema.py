from typing_extensions import Literal
from pydantic import BaseModel, validator, ValidationError
from datetime import date
from typing import Optional, Literal

class CompanyBase(BaseModel):
    name: str
    start_year: date
    cuit: str
    legal_status: Optional[
        Literal[
            "S.A.",
            "S.R.L.",
            "S.A.S.",
            "Sociedad de Hecho",
            "Cooperativa",
            "Asociación Civil",
            "Unipersonal/Monotributista"
            ]
        ] = "Unipersonal/Monotributista"
    annual_revenue: int
    fixed_employees: int
    temporary_employees: int
    productions: int
    funding_source: Optional[
        Literal[
            "Fondos Propios",
            "Coproducciones con asociados nacionales",
            "Coproducciones con asociados internacionales",
            "Fondos INCAA",
            "Fondos IAAviM",
            "Fondos Provinciales o Municipales",
            "Financiamiento de Organismos Internacionales o Premios de festivales",
            "Ventas a mercados internacionales",
            "Ventas en el mercado nacional",
            "Servicios a terceros nacionales",
            "Servicios a terceros internacionales",
            "Donaciones",
            "préstamos",
            "legados",
            "Otros"
        ]
    ] = "Fondos Propios"

class CompanyCreate(CompanyBase):
    pass

class CompanyOut(CompanyBase):
    id: int
    user_email: str

    class Config:
        from_attributes = True
