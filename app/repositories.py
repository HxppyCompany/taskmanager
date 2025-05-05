from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from . import models

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_task(self, task: models.Task) -> models.Task:
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_task(self, task_id: int) -> models.Task | None:
        return self.db.query(models.Task).filter(models.Task.id == task_id).first()

    def update_progress(self, task_id: int, progress: float) -> models.Task | None:
        task = self.get_task(task_id)
        if task:
            task.progress = progress
            self.db.commit()
            self.db.refresh(task)
        return task

    def get_all_tasks(self) -> List[models.Task]:
        return self.db.query(models.Task).all()

    def get_incomplete_tasks(self) -> List[models.Task]:
        return self.db.query(models.Task).filter(models.Task.progress < 100).all()

    def get_overdue_tasks(self, now: datetime) -> List[models.Task]:
        return self.db.query(models.Task).filter(
            models.Task.due_date != None,
            models.Task.due_date < now,
            models.Task.progress < 100
        ).all()
