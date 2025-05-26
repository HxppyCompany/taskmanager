from datetime import datetime
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, models, repositories
from .logger import logger


class TaskService:
    def __init__(self, session: AsyncSession):
        self.repo = repositories.TaskRepository(session)

    async def create_task(self, task_create: schemas.TaskCreate) -> models.Task:
        logger.info(f"Создание задачи: {task_create.title}")
        task = models.Task(
            title=task_create.title,
            description=task_create.description,
            progress=task_create.progress or 0.0,
            due_date=task_create.due_date,
            created_at=datetime.utcnow()
        )
        result = await self.repo.add_task(task)
        logger.debug(f"Задача создана с id={result.id}")
        return result

    async def update_progress(self, task_id: int, progress: float) -> models.Task | None:
        logger.info(f"Обновление прогресса задачи id={task_id} до {progress}%")
        task = await self.repo.update_progress(task_id, progress)
        if task:
            logger.debug(f"Прогресс задачи id={task_id} обновлен")
        else:
            logger.warning(
                f"Задача id={task_id} не найдена для обновления прогресса")
        return task

    async def get_all_tasks(self) -> List[models.Task]:
        return await self.repo.get_all_tasks()

    async def get_incomplete_tasks(self) -> List[models.Task]:
        return await self.repo.get_incomplete_tasks()

    async def get_overdue_tasks(self) -> List[models.Task]:
        return await self.repo.get_overdue_tasks()
