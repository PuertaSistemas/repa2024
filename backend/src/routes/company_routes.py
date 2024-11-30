from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.auth.permissions import has_role
from src.db.database import get_db
from src.models.company_model import Company
from src.schemas.company_schema import CompanyCreate, CompanyOut
from src.models.user_model import User

company_router = APIRouter()

# Crear una nueva compañía
@company_router.post("/", response_model=CompanyOut)
def create_company(
    company: CompanyCreate, db: Session = Depends(get_db), current_user: User = Depends(has_role(["admin", "editor"]))):
    new_company = Company(**company.dict(), user_email=current_user.email)
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company

# Listar compañías asociadas al usuario autenticado
@company_router.get("/", response_model=list[CompanyOut])
def list_companies(db: Session = Depends(get_db),current_user: User = Depends(has_role(["admin", "editor"]))):
    # Si es editor, listar empresas relacionadas con el usuario
    if has_role(["admin"]):
        company = db.query(Company).all()
    else:
        company = db.query(Company).filter(Company.user_email == current_user.email).all()
    return company

# Obtener detalles de una compañía por ID
@company_router.get("/{company_id}", response_model=CompanyOut)
def get_company(
    company_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(has_role(["admin", "editor"]))
):
    if has_role(["admin"]):
        company = db.query(Company).filter(Company.id == company_id).first()
    else:
        company = db.query(Company).filter(Company.id == company_id, Company.user_email == current_user.email).first()

    if not company:
        raise HTTPException(status_code=404, detail="Compañía no encontrada")
    return company

# Eliminar una compañía
@company_router.delete("/{company_id}")
def delete_company(
    company_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(has_role(["admin", "editor"]))
):
    if has_role(["admin"]):
        company = db.query(Company).filter(Company.id == company_id).first()
    else:
        company = db.query(Company).filter(Company.id == company_id, Company.user_email == current_user.email).first()

    if not company:
        raise HTTPException(status_code=404, detail="Compañía no encontrada")

    db.delete(company)
    db.commit()
    return {"message": "Compañía eliminada correctamente"}
