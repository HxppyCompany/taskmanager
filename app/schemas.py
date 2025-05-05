from pydantic import BaseModel, Field, confloat
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: str = Field(..., max_length=100)
    description: Optional[str] = None
    progress: Optional[confloat(ge=0, le=100)] = 0.0
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdateProgress(BaseModel):
    progress: confloat(ge=0, le=100)

class TaskInDB(TaskBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
