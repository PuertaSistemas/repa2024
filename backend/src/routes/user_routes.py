from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from src.auth.auth import create_access_token, verify_token
from src.models.user_model import User
from src.schemas.user_schema import UserCreate, UserOut
from src.db.database import get_db
from passlib.context import CryptContext
from datetime import datetime

user_router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

# Ruta para iniciar sesión
@user_router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

# Dependencia para validar usuarios autenticados
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

    email: str = payload.get("sub")
    if not email:
        raise HTTPException(status_code=401, detail="Token inválido")

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    return user

# Ruta protegida de ejemplo
@user_router.get("/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

# Crear un usuario
@user_router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    hashed_password = pwd_context.hash(user.password)
    new_user = User(
        email=user.email,
        hashed_password=hashed_password,
        is_admin=user.is_admin,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Obtener un usuario por email
@user_router.get("/{email}", response_model=UserOut)
def get_user(email: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

# Actualizar último acceso
@user_router.patch("/{email}/last-login", response_model=UserOut)
def update_last_login(email: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db_user.last_login = datetime.utcnow()
    db.commit()
    db.refresh(db_user)
    return db_user

# Eliminar un usuario
@user_router.delete("/{email}")
def delete_user(email: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(db_user)
    db.commit()
    return {"message": "Usuario eliminado correctamente"}
