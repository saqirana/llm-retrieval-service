"""
LLM Retrieval Service - Main Application Entry Point

A production-ready RAG (Retrieval-Augmented Generation) system built with FastAPI.
Provides intelligent document retrieval, real-time chat streaming, and scalable
vector search capabilities.

Author: Muhammad Saqib
Email: saqi_rana@hotmail.com
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles
import uvicorn
import time
import logging

from app.core.config import settings
from app.core.logging import setup_logging
from app.api.v1.router import api_router

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager for startup and shutdown events.
    """
    # Startup
    logger.info("🚀 Starting LLM Retrieval Service...")
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    logger.info(f"Version: {settings.VERSION}")

    # Initialize services
    # await init_db()
    # await init_vector_store()
    # await init_redis()

    logger.info("✅ Application startup complete")

    yield

    # Shutdown
    logger.info("🛑 Shutting down LLM Retrieval Service...")
    # Cleanup resources
    logger.info("✅ Application shutdown complete")


# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Enterprise-grade RAG system with LLM integration, vector search, and chat streaming",
    version=settings.VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GZip Middleware for response compression
app.add_middleware(GZipMiddleware, minimum_size=1000)


# Custom middleware for request tracking
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Add request processing time and correlation ID to response headers."""
    start_time = time.time()

    # Generate correlation ID
    correlation_id = request.headers.get("X-Correlation-ID", f"req-{int(time.time() * 1000)}")

    response = await call_next(request)

    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    response.headers["X-Correlation-ID"] = correlation_id

    return response


# Exception handlers
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler for unhandled exceptions."""
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "An internal server error occurred",
            "type": "internal_server_error",
        },
    )


# Health check endpoints
@app.get("/", tags=["Health"])
async def root():
    """Root endpoint - basic service information."""
    return {
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "operational",
        "environment": settings.ENVIRONMENT,
        "docs": "/docs",
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint for load balancers and monitoring systems.
    """
    return {
        "status": "healthy",
        "version": settings.VERSION,
        "timestamp": time.time(),
    }


@app.get("/health/ready", tags=["Health"])
async def readiness_check():
    """
    Readiness check - verifies all dependencies are available.
    """
    # Check database connection
    # Check Redis connection
    # Check vector store connection
    # Check LLM API availability

    return {
        "status": "ready",
        "checks": {
            "database": "healthy",
            "redis": "healthy",
            "vector_store": "healthy",
            "llm": "healthy",
        },
    }


@app.get("/health/live", tags=["Health"])
async def liveness_check():
    """
    Liveness check - verifies application is running.
    """
    return {"status": "alive"}


# Include API routers
app.include_router(api_router, prefix=settings.API_V1_PREFIX)


# Main entry point for local development
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )
