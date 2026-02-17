"""
Unit tests for authentication endpoints.
"""

import pytest
from fastapi.testclient import TestClient


@pytest.mark.unit
def test_register_user(client: TestClient):
    """Test user registration."""
    response = client.post(
        "/api/v1/auth/register",
        params={
            "email": "test@example.com",
            "password": "SecurePassword123!",
            "full_name": "Test User"
        }
    )

    assert response.status_code == 201
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.unit
def test_login(client: TestClient):
    """Test user login."""
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "test@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data


@pytest.mark.unit
def test_get_current_user(client: TestClient, auth_headers):
    """Test getting current user information."""
    response = client.get("/api/v1/auth/me", headers=auth_headers)

    assert response.status_code == 200
    data = response.json()
    assert "email" in data
    assert "role" in data

