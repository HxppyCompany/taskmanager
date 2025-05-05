from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from ..schemas import TaskCreate, TaskUpdateProgress, TaskInDB
from ..controllers import TaskController
from ..repositories import TaskRepository
from ..dependencies import get_task_repository

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=TaskInDB, status_code=status.HTTP_201_CREATED)
def create_task(
    task_create: TaskCreate,
    repo: TaskRepository = Depends(get_task_repository)
):
    controller = TaskController(repo)
    return controller.create_task(task_create)

@router.patch("/{task_id}/progress", response_model=TaskInDB)
def update_progress(
    task_id: int,
    progress_update: TaskUpdateProgress,
    repo: TaskRepository = Depends(get_task_repository)
):
    controller = TaskController(repo)
    task = controller.update_task_progress(task_id, progress_update.progress)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("/", response_model=List[TaskInDB])
def get_all_tasks(
    repo: TaskRepository = Depends(get_task_repository)
):
    controller = TaskController(repo)
    return controller.list_all_tasks()

@router.get("/incomplete", response_model=List[TaskInDB])
def get_incomplete_tasks(
    repo: TaskRepository = Depends(get_task_repository)
):
    controller = TaskController(repo)
    return controller.list_incomplete_tasks()

@router.get("/overdue", response_model=List[TaskInDB])
def get_overdue_tasks(
    repo: TaskRepository = Depends(get_task_repository)
):
    controller = TaskController(repo)
    return controller.list_overdue_tasks()
