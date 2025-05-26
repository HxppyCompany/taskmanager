from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .database import AsyncSessionLocal
from .services import TaskService


async def get_async_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


async def get_task_service(
    session: AsyncSession = Depends(get_async_session),
) -> TaskService:
    return TaskService(session)
