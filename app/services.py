from datetime import datetime
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

class TaskService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_task(self, task_data: schemas.TaskCreate) -> models.Task:
        new_task = models.Task(
            **task_data.model_dump(),
            created_at=datetime.utcnow()
        )
        self.session.add(new_task)
        await self.session.commit()
        return new_task

    async def update_progress(self, task_id: int, progress: float) -> models.Task | None:
        task = await self.session.get(models.Task, task_id)
        if task:
            task.progress = progress
            await self.session.commit()
        return task
