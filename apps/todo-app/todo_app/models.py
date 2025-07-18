"""Database models for the Todo App."""

from sqlalchemy import Column, String, Boolean, Text
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../packages"))
from shared.database import BaseModel

class Todo(BaseModel):
    """Todo model for storing tasks."""
    __tablename__ = "todos"
    
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
    priority = Column(String(10), default="medium", nullable=False)  # low, medium, high
    
    def to_dict(self):
        """Convert todo to dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "priority": self.priority,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }