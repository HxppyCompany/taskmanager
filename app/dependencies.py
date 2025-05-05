from fastapi import Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .repositories import TaskRepository

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_task_repository(db: Session = Depends(get_db)) -> TaskRepository:
    return TaskRepository(db)
