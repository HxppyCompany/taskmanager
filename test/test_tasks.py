import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_create_task():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/tasks/",
            json={
                "title": "Test Task",
                "description": "Описание тестовой задачи",
                "progress": 0,
                "due_date": None,
            },
        )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["progress"] == 0
