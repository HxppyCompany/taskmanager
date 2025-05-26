from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from .. import schemas
from ..services import TaskService
from ..dependencies import get_task_service

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=schemas.TaskInDB, status_code=status.HTTP_201_CREATED)
async def create_task(
    task: schemas.TaskCreate, service: TaskService = Depends(get_task_service)
):
    return await service.create_task(task)


@router.patch("/{task_id}/progress", response_model=schemas.TaskInDB)
async def update_progress(
    task_id: int,
    progress_update: schemas.TaskUpdateProgress,
    service: TaskService = Depends(get_task_service),
):
    updated_task = await service.update_progress(task_id, progress_update.progress)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@router.get("/", response_model=List[schemas.TaskInDB])
async def get_all_tasks(service: TaskService = Depends(get_task_service)):
    return await service.get_all_tasks()


@router.get("/incomplete", response_model=List[schemas.TaskInDB])
async def get_incomplete_tasks(service: TaskService = Depends(get_task_service)):
    return await service.get_incomplete_tasks()


@router.get("/overdue", response_model=List[schemas.TaskInDB])
async def get_overdue_tasks(service: TaskService = Depends(get_task_service)):
    return await service.get_overdue_tasks()
