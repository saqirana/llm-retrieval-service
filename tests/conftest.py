"""
Test configuration and fixtures.
"""

import pytest
from typing import Generator, AsyncGenerator
from fastapi.testclient import TestClient
from httpx import AsyncClient
import asyncio

from main import app


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def client() -> Generator:
    """
    Create a test client for the FastAPI application.
    """
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
async def async_client() -> AsyncGenerator:
    """
    Create an async test client for the FastAPI application.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def mock_openai_response():
    """Mock OpenAI API response."""
    return {
        "id": "chatcmpl-123",
        "object": "chat.completion",
        "created": 1677652288,
        "model": "gpt-4-turbo-preview",
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "This is a test response"
            },
            "finish_reason": "stop"
        }],
        "usage": {
            "prompt_tokens": 9,
            "completion_tokens": 12,
            "total_tokens": 21
        }
    }


@pytest.fixture
def sample_jwt_token():
    """Generate a sample JWT token for testing."""
    from app.core.security import create_access_token

    return create_access_token(
        data={"sub": "test@example.com", "role": "user"}
    )


@pytest.fixture
def auth_headers(sample_jwt_token):
    """Create authentication headers with JWT token."""
    return {
        "Authorization": f"Bearer {sample_jwt_token}"
    }

