"""
Health Check Endpoints
Provides health, readiness, and liveness checks.
"""

from fastapi import APIRouter, status
from typing import Dict, Any
import time

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def health_check() -> Dict[str, Any]:
    """
    Basic health check endpoint.
    Returns the service status and version.
    """
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "version": "1.0.0",
    }


@router.get("/ready", status_code=status.HTTP_200_OK)
async def readiness_check() -> Dict[str, Any]:
    """
    Readiness probe for Kubernetes/ECS.
    Checks if all dependencies are available.
    """
    # TODO: Add actual dependency checks
    # - Database connection
    # - Redis connection
    # - Vector store connection
    # - LLM API availability

    checks = {
        "database": "healthy",
        "redis": "healthy",
        "vector_store": "healthy",
        "llm": "healthy",
    }

    all_healthy = all(status == "healthy" for status in checks.values())

    return {
        "status": "ready" if all_healthy else "not_ready",
        "checks": checks,
        "timestamp": time.time(),
    }


@router.get("/live", status_code=status.HTTP_200_OK)
async def liveness_check() -> Dict[str, Any]:
    """
    Liveness probe for Kubernetes/ECS.
    Checks if the application is running.
    """
    return {
        "status": "alive",
        "timestamp": time.time(),
    }

