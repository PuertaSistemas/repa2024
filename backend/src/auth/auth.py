from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

# Librerias necesarias para la función get_current_user de validacion del usuario
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from src.models.user_model import User
from fastapi.security import OAuth2PasswordBearer
from src.db.database import get_db

# Configuración de JWT
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY") # Cambia esto a un valor seguro
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30 #os.getenv(ACCESS_TOKEN_EXPIRE_MINUTES)

# Objeto necesario para la función de 'get_current_user' que valida los datos del usuario
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

# Generar un token JWT
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Verificar y decodificar un token JWT
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

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
