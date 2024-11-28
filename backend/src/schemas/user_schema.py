from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    is_admin: bool

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    created_at: datetime
    last_login: Optional[datetime]

class Token(BaseModel):
    access_token: str
    token_type: str
