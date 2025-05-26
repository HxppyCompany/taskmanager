from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from datetime import datetime
from typing import List
from . import models


class TaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_task(self, task: models.Task) -> models.Task:
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def get_task(self, task_id: int) -> models.Task | None:
        result = await self.session.get(models.Task, task_id)
        return result

    async def update_progress(
        self, task_id: int, progress: float
    ) -> models.Task | None:
        task = await self.get_task(task_id)
        if task:
            task.progress = progress
            await self.session.commit()
            await self.session.refresh(task)
        return task

    async def get_all_tasks(self) -> List[models.Task]:
        result = await self.session.execute(select(models.Task))
        return result.scalars().all()

    async def get_incomplete_tasks(self) -> List[models.Task]:
        stmt = select(models.Task).where(models.Task.progress < 100)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_overdue_tasks(self) -> List[models.Task]:
        now = datetime.utcnow()
        stmt = select(models.Task).where(
            and_(
                models.Task.due_date != None,
                models.Task.due_date < now,
                models.Task.progress < 100,
            )
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()
