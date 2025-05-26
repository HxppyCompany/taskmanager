# app/routers/tasks.py
from fastapi import APIRouter, Depends, HTTPException
from .schemas import TaskCreate, TaskUpdate
from .services import TaskService
from .dependencies import get_async_session

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("")
async def create_task(data: TaskCreate, service: TaskService = Depends(TaskService)):
    try:
        return await service.create_task(data)
    except Exception as e:
        raise HTTPException(500, str(e))
