"""State management for Todo App."""

import reflex as rx
from typing import List, Dict, Any
from .database import get_db_session, init_db
from .models import Todo

class TodoState(rx.State):
    """State for managing todos."""
    
    todos: List[Dict[str, Any]] = []
    new_todo_title: str = ""
    new_todo_description: str = ""
    new_todo_priority: str = "medium"
    filter_status: str = "all"  # all, completed, pending
    filter_priority: str = "all"  # all, low, medium, high
    is_loading: bool = False
    error_message: str = ""
    success_message: str = ""
    
    def __init__(self):
        super().__init__()
        self.load_todos()
    
    def load_todos(self):
        """Load todos from database."""
        try:
            init_db()
            db = get_db_session()
            todos = db.query(Todo).order_by(Todo.created_at.desc()).all()
            self.todos = [todo.to_dict() for todo in todos]
            db.close()
        except Exception as e:
            self.error_message = f"Failed to load todos: {str(e)}"
    
    def add_todo(self):
        """Add a new todo."""
        if not self.new_todo_title.strip():
            self.error_message = "Title is required"
            return
        
        try:
            self.is_loading = True
            db = get_db_session()
            
            new_todo = Todo(
                title=self.new_todo_title.strip(),
                description=self.new_todo_description.strip(),
                priority=self.new_todo_priority,
                completed=False
            )
            
            db.add(new_todo)
            db.commit()
            db.refresh(new_todo)
            
            self.todos.insert(0, new_todo.to_dict())
            self.new_todo_title = ""
            self.new_todo_description = ""
            self.new_todo_priority = "medium"
            self.success_message = "Todo added successfully!"
            self.error_message = ""
            
            db.close()
        except Exception as e:
            self.error_message = f"Failed to add todo: {str(e)}"
        finally:
            self.is_loading = False
    
    def toggle_todo(self, todo_id: int):
        """Toggle todo completion status."""
        try:
            db = get_db_session()
            todo = db.query(Todo).filter(Todo.id == todo_id).first()
            
            if todo:
                todo.completed = not todo.completed
                db.commit()
                
                for i, t in enumerate(self.todos):
                    if t["id"] == todo_id:
                        self.todos[i]["completed"] = todo.completed
                        break
                
                self.success_message = "Todo updated successfully!"
            
            db.close()
        except Exception as e:
            self.error_message = f"Failed to update todo: {str(e)}"
    
    def delete_todo(self, todo_id: int):
        """Delete a todo."""
        try:
            db = get_db_session()
            todo = db.query(Todo).filter(Todo.id == todo_id).first()
            
            if todo:
                db.delete(todo)
                db.commit()
                
                self.todos = [t for t in self.todos if t["id"] != todo_id]
                self.success_message = "Todo deleted successfully!"
            
            db.close()
        except Exception as e:
            self.error_message = f"Failed to delete todo: {str(e)}"
    
    def set_new_todo_title(self, title: str):
        """Set new todo title."""
        self.new_todo_title = title
        self.error_message = ""
    
    def set_new_todo_description(self, description: str):
        """Set new todo description."""
        self.new_todo_description = description
    
    def set_new_todo_priority(self, priority: str):
        """Set new todo priority."""
        self.new_todo_priority = priority
    
    def set_filter_status(self, status: str):
        """Set filter status."""
        self.filter_status = status
    
    def set_filter_priority(self, priority: str):
        """Set filter priority."""
        self.filter_priority = priority
    
    def clear_messages(self):
        """Clear success and error messages."""
        self.success_message = ""
        self.error_message = ""
    
    @rx.var
    def filtered_todos(self) -> List[Dict[str, Any]]:
        """Get filtered todos based on current filters."""
        filtered = self.todos
        
        if self.filter_status == "completed":
            filtered = [t for t in filtered if t["completed"]]
        elif self.filter_status == "pending":
            filtered = [t for t in filtered if not t["completed"]]
        
        if self.filter_priority != "all":
            filtered = [t for t in filtered if t["priority"] == self.filter_priority]
        
        return filtered
    
    @rx.var
    def todos_count(self) -> Dict[str, int]:
        """Get count of todos by status."""
        total = len(self.todos)
        completed = len([t for t in self.todos if t["completed"]])
        pending = total - completed
        
        return {
            "total": total,
            "completed": completed,
            "pending": pending
        }