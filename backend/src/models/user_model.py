from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from src.db.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, index=True)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="viewer")  # Define roles: admin, editor, viewer, etc.
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime, default=None, nullable=True)
