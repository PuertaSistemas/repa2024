from pydantic import BaseModel
from datetime import date
from typing import Optional

class CompanyBase(BaseModel):
    name: str
    start_year: date
    cuit: str
    legal_status: str
    annual_revenue: int
    fixed_employees: int
    temporary_employees: int
    productions: int
    funding_source: int

class CompanyCreate(CompanyBase):
    pass

class CompanyOut(CompanyBase):
    id: int
    user_email: str

    class Config:
        from_attributes = True
