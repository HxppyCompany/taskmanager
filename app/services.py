from datetime import datetime
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, models, repositories


class TaskService:
    def __init__(self, session: AsyncSession):
        self.repo = repositories.TaskRepository(session)

    async def create_task(self, task_create: schemas.TaskCreate) -> models.Task:
        task = models.Task(
            title=task_create.title,
            description=task_create.description,
            progress=task_create.progress or 0.0,
            due_date=task_create.due_date,
            created_at=datetime.utcnow(),
        )
        return await self.repo.add_task(task)

    async def update_progress(
        self, task_id: int, progress: float
    ) -> models.Task | None:
        return await self.repo.update_progress(task_id, progress)

    async def get_all_tasks(self) -> List[models.Task]:
        return await self.repo.get_all_tasks()

    async def get_incomplete_tasks(self) -> List[models.Task]:
        return await self.repo.get_incomplete_tasks()

    async def get_overdue_tasks(self) -> List[models.Task]:
        return await self.repo.get_overdue_tasks()
