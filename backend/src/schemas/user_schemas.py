from pydantic import BaseModel, Field, validator
import datetime

class User(BaseModel):
    id: int
    name: str
    email: str

class UserCreate(BaseModel):
    id: int
    name: str
    email: str

class UserUpdate(BaseModel):
    name: str
