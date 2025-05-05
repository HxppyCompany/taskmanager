from fastapi import FastAPI
from .database import Base, engine
from .routers import tasks

app = FastAPI(title="Task Tracker")

# Создаем таблицы в БД при запуске
Base.metadata.create_all(bind=engine)

app.include_router(tasks.router)
