"""
API Router Configuration
Aggregates all endpoint routers.
"""

from fastapi import APIRouter

from app.api.v1.endpoints import auth, chat, documents, retrieval, health

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(health.router, prefix="/health", tags=["Health"])
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(documents.router, prefix="/documents", tags=["Documents"])
api_router.include_router(retrieval.router, prefix="/retrieval", tags=["Retrieval"])
api_router.include_router(chat.router, prefix="/chat", tags=["Chat"])

