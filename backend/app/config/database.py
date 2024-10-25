import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("POSTGRES_DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Generator for a local database session.

    Yields a database session to be used by FastAPI's dependency injection system.
    Closes the session when it is no longer needed.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
