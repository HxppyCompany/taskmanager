# app/repositories.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, or_
from datetime import datetime


class TaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_overdue(self) -> list[models.Task]:
        result = await self.session.execute(
            select(models.Task).where(
                and_(
                    models.Task.due_date < datetime.utcnow(), models.Task.progress < 100
                )
            )
        )
        return result.scalars().all()
