from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    role: str  # El rol del usuario

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    created_at: datetime
    last_login: Optional[datetime]

class Token(BaseModel):
    access_token: str
    token_type: str
