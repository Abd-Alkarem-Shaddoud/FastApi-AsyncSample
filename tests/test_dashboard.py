#python -m pytest -q

import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_dashboard_endpoint():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as ac:

        response = await ac.get("/dashboard/1")

    assert response.status_code == 200

    response_data = response.json()
    assert "user_data" in response_data
    assert "orders_data" in response_data
    assert "external_data" in response_data