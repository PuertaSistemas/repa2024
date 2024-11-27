from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_USER= os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD= os.getenv("POSTGRES_PASSWORD")
POSTGRES_PORT= os.getenv("POSTGRES_PORT")
POSTGRES_DB= os.getenv("POSTGRES_DB")
POSTGRES_DBHOST=os.getenv("POSTGRES_DBHOST")

DATABASE_URL = 'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_DBHOST}:5432/{POSTGRES_DB}'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()
