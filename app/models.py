from sqlalchemy import String, Text, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from .database import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    progress: Mapped[float] = mapped_column(default=0.0)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    due_date: Mapped[datetime | None] = mapped_column(nullable=True)
