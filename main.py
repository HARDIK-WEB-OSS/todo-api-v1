"""
Simple Todo API - Version 1 (MVP)
Deploy this TODAY before building anything more complex
"""
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import models
from database import engine, get_db
from pydantic import BaseModel
from datetime import datetime

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo API v1",
    description="Simple CRUD Todo API",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic schemas
class TodoCreate(BaseModel):
    title: str
    description: str = ""

class TodoUpdate(BaseModel):
    title: str = None
    description: str = None
    completed: bool = None

class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Routes
@app.get("/")
def root():
    return {
        "message": "Todo API v1",
        "endpoints": {
            "create": "POST /todos",
            "list": "GET /todos",
            "get": "GET /todos/{id}",
            "update": "PUT /todos/{id}",
            "delete": "DELETE /todos/{id}",
            "toggle": "PATCH /todos/{id}/toggle"
        }
    }

@app.post("/todos", response_model=TodoResponse, status_code=201)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    """Create a new todo"""
    db_todo = models.Todo(
        title=todo.title,
        description=todo.description
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.get("/todos", response_model=List[TodoResponse])
def get_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all todos"""
    todos = db.query(models.Todo).offset(skip).limit(limit).all()
    return todos

@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    """Get a specific todo"""
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo_update: TodoUpdate, db: Session = Depends(get_db)):
    """Update a todo"""
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    if todo_update.title is not None:
        todo.title = todo_update.title
    if todo_update.description is not None:
        todo.description = todo_update.description
    if todo_update.completed is not None:
        todo.completed = todo_update.completed
    
    db.commit()
    db.refresh(todo)
    return todo

@app.patch("/todos/{todo_id}/toggle", response_model=TodoResponse)
def toggle_todo(todo_id: int, db: Session = Depends(get_db)):
    """Toggle todo completion status"""
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo.completed = not todo.completed
    db.commit()
    db.refresh(todo)
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a todo"""
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully"}

@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    """Get statistics"""
    total = db.query(models.Todo).count()
    completed = db.query(models.Todo).filter(models.Todo.completed == True).count()
    pending = total - completed
    
    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "completion_rate": round((completed / total * 100) if total > 0 else 0, 2)
    }

if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*50)
    print("🚀 Server starting...")
    print("📍 Visit: http://localhost:8000/docs")
    print("="*50 + "\n")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)