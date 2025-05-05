from datetime import datetime
from typing import List
from .schemas import TaskCreate, TaskUpdateProgress, TaskInDB
from .repositories import TaskRepository
from .models import Task

class TaskController:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, task_create: TaskCreate) -> TaskInDB:
        task = Task(
            title=task_create.title,
            description=task_create.description,
            progress=task_create.progress or 0.0,
            due_date=task_create.due_date,
            created_at=datetime.utcnow()
        )
        task = self.repository.add_task(task)
        return TaskInDB.from_orm(task)

    def update_task_progress(self, task_id: int, progress: float) -> TaskInDB | None:
        task = self.repository.update_progress(task_id, progress)
        if task:
            return TaskInDB.from_orm(task)
        return None

    def list_all_tasks(self) -> List[TaskInDB]:
        tasks = self.repository.get_all_tasks()
        return [TaskInDB.from_orm(task) for task in tasks]

    def list_incomplete_tasks(self) -> List[TaskInDB]:
        tasks = self.repository.get_incomplete_tasks()
        return [TaskInDB.from_orm(task) for task in tasks]

    def list_overdue_tasks(self) -> List[TaskInDB]:
        now = datetime.utcnow()
        tasks = self.repository.get_overdue_tasks(now)
        return [TaskInDB.from_orm(task) for task in tasks]
