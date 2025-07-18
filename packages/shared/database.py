"""Shared database utilities using SQLAlchemy and SQLite."""

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

Base = declarative_base()

def get_database_url(app_name: str) -> str:
    """Get database URL for the given app."""
    db_dir = os.path.join(os.getcwd(), "data")
    os.makedirs(db_dir, exist_ok=True)
    return f"sqlite:///{db_dir}/{app_name}.db"

def create_database_engine(app_name: str):
    """Create database engine for the given app."""
    database_url = get_database_url(app_name)
    engine = create_engine(
        database_url,
        connect_args={"check_same_thread": False},
        echo=False
    )
    return engine

def get_session_maker(engine):
    """Get session maker for database operations."""
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

class BaseModel(Base):
    """Base model with common fields."""
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)