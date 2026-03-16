"""Tests for API endpoints."""

import pytest
from httpx import AsyncClient, ASGITransport
from analytix.main import app


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_health_check(client):
    response = await client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


@pytest.mark.asyncio
async def test_analyze_endpoint(client):
    response = await client.post(
        "/api/v1/analyze",
        json={"data": [10, 20, 30, 40, 50], "operations": ["describe"]},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["results"]["mean"] == 30.0
    assert data["sample_size"] == 5


@pytest.mark.asyncio
async def test_analyze_empty_data(client):
    response = await client.post("/api/v1/analyze", json={"data": []})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_detect_anomalies(client):
    response = await client.post(
        "/api/v1/detect",
        json={"data": [10, 12, 11, 13, 12, 100], "method": "zscore"},
    )
    assert response.status_code == 200
    data = response.json()
    assert 100 in data["outliers"]
