"""
Authentication Endpoints
Handles user registration, login, token refresh, and logout.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Dict, Any
from datetime import timedelta

from app.core.config import settings
from app.core.security import (
    create_access_token,
    create_refresh_token,
    get_password_hash,
    verify_password,
    decode_token,
    get_current_user,
)

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    email: str,
    password: str,
    full_name: str = None,
) -> Dict[str, Any]:
    """
    Register a new user.

    Args:
        email: User email address
        password: User password
        full_name: Optional full name

    Returns:
        User information and tokens
    """
    # TODO: Check if user already exists in database
    # TODO: Create user in database

    # Hash password
    hashed_password = get_password_hash(password)

    # Create tokens
    access_token = create_access_token(
        data={"sub": email, "role": "user"}
    )
    refresh_token = create_refresh_token(
        data={"sub": email}
    )

    return {
        "message": "User registered successfully",
        "user": {
            "email": email,
            "full_name": full_name,
        },
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Dict[str, Any]:
    """
    Login and get access token.

    Args:
        form_data: OAuth2 password request form

    Returns:
        Access token and refresh token
    """
    # TODO: Get user from database
    # TODO: Verify password

    # For now, mock authentication
    email = form_data.username

    # Create tokens
    access_token = create_access_token(
        data={"sub": email, "role": "user"}
    )
    refresh_token = create_refresh_token(
        data={"sub": email}
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    }


@router.post("/refresh")
async def refresh_token(refresh_token: str) -> Dict[str, Any]:
    """
    Refresh access token using refresh token.

    Args:
        refresh_token: Valid refresh token

    Returns:
        New access token
    """
    payload = decode_token(refresh_token)

    if payload.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token type"
        )

    email = payload.get("sub")

    # Create new access token
    access_token = create_access_token(
        data={"sub": email, "role": "user"}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    }


@router.get("/me")
async def get_current_user_info(
    current_user: Dict[str, Any] = Depends(get_current_user)
) -> Dict[str, Any]:
    """
    Get current user information.

    Args:
        current_user: Current authenticated user

    Returns:
        User information
    """
    return {
        "email": current_user.get("sub"),
        "role": current_user.get("role", "user"),
    }


@router.post("/logout")
async def logout(
    current_user: Dict[str, Any] = Depends(get_current_user)
) -> Dict[str, str]:
    """
    Logout current user.

    Args:
        current_user: Current authenticated user

    Returns:
        Success message
    """
    # TODO: Invalidate token (add to blacklist in Redis)

    return {
        "message": "Successfully logged out"
    }

