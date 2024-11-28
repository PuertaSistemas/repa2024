from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.models.user_model import User
from src.auth.auth import get_current_user

def has_role(required_roles: list[str]):
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role not in required_roles:
            raise HTTPException(status_code=403, detail="No tienes permisos para acceder a este recurso")
        return current_user
    return role_checker
