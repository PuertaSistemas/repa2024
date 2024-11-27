from sqlalchemy import Column, Integer, String
from src.db.connectdb import Base

# clase
class User(Base):
    # nombre de la tabla
    __tablename__ = "user"

    # Las columnas de nuestra tabla y el tipo de dato de cada una
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

#class UserCreate(User):
    # Las columnas de nuestra tabla y el tipo de dato de cada una
#    id = Column(Integer, primary_key=True)
#    name = Column(String)
#    email = Column(String)

#class UserUpdate(Base):
    # Las columnas de nuestra tabla y el tipo de dato de cada una
#    name = Column(String)
