"""Database setup for Todo App."""

import sys
import os
from sqlalchemy.orm import Session

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../packages"))
from shared.database import create_database_engine, get_session_maker, Base
from .models import Todo

engine = create_database_engine("todo_app")
SessionLocal = get_session_maker(engine)

def init_db():
    """Initialize the database."""
    Base.metadata.create_all(bind=engine)

def get_db() -> Session:
    """Get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_db_session() -> Session:
    """Get database session for direct use."""
    return SessionLocal()