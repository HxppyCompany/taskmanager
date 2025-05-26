from fastapi import FastAPI
from .database import engine, Base
from .routers import tasks

app = FastAPI(title="Task Tracker")


@app.on_event("startup")
async def on_startup():
    # Создаем таблицы в БД при старте
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(tasks.router)
