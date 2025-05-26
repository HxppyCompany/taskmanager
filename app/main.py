from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from .logger import logger
from .database import engine, Base
from .routers import tasks

app = FastAPI(title="Task Tracker")


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(tasks.router)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger.info(f"Запрос: {request.method} {request.url}")
        response = await call_next(request)
        logger.info(
            f"Ответ: {response.status_code} для {request.method} {request.url}")
        return response


app.add_middleware(LoggingMiddleware)
