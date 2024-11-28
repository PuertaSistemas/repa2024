from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from src.auth.auth import create_access_token, verify_token, get_current_user # Se mueve la funcion 'get_current_user' a la libreria de 'auth'
from src.auth.permissions import has_role
from src.models.user_model import User
from src.schemas.user_schema import UserCreate, UserOut
from src.db.database import get_db
from passlib.context import CryptContext
from datetime import datetime

user_router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

# Actualizar último acceso... Esto se debe integrar a la ruta de logín del usuario.
# @user_router.patch("/{email}/last-login", response_model=UserOut)
def update_last_login(email: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db_user.last_login = datetime.utcnow()
    db.commit()
    db.refresh(db_user)
    #return db_user

# Ruta para iniciar sesión Verificar ésta ruta....
@user_router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    token = create_access_token(data={"sub": user.email})
    # Actualizar el registro de last_login del usuario...
    update_last_login(User.email, db)
    return {"access_token": token, "token_type": "bearer"}

# Ruta protegida de ejemplo
@user_router.get("/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

# Listar todos los usuarios, solo para los administradores (ejemplo)
@user_router.get("/", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db), current_user: User = Depends(has_role(["admin"]))):
    # Solo los administradores pueden ver la lista completa
    return db.query(User).all()

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
        role=user.role,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Obtener un usuario por email
@user_router.get("/{email}", response_model=UserOut)
def get_user(email: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Los administradores pueden acceder a cualquier usuario
    if not current_user.is_admin and current_user.email != email:
        raise HTTPException(status_code=403, detail="No tienes permisos para acceder a este usuario")

    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

# Eliminar un usuario siempre el el email del current:user sea igual al del token
@user_router.delete("/{email}")
def delete_user(email: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(db_user)
    db.commit()
    return {"message": "Usuario eliminado correctamente"}
