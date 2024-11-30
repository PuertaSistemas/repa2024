from sqlalchemy import Column, String, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base

class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    start_year = Column(Date, nullable=False)
    cuit = Column(String, nullable=False, unique=True)
    legal_status = Column(String, nullable=False)
    annual_revenue = Column(Integer, nullable=True)
    fixed_employees = Column(Integer, nullable=True)
    temporary_employees = Column(Integer, nullable=True)
    productions = Column(Integer, nullable=True)
    funding_source = Column(Integer, nullable=True)

    user_email = Column(String, ForeignKey("users.email"))
    user = relationship("User", back_populates="company")
