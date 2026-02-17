"""
Unit tests for health check endpoints.
"""

import pytest
from fastapi.testclient import TestClient


@pytest.mark.unit
def test_health_check(client: TestClient):
    """Test basic health check endpoint."""
    response = client.get("/api/v1/health/")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "version" in data


@pytest.mark.unit
def test_readiness_check(client: TestClient):
    """Test readiness check endpoint."""
    response = client.get("/api/v1/health/ready")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ready"
    assert "checks" in data
    assert "timestamp" in data


@pytest.mark.unit
def test_liveness_check(client: TestClient):
    """Test liveness check endpoint."""
    response = client.get("/api/v1/health/live")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "alive"
    assert "timestamp" in data

