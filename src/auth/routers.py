from fastapi import APIRouter

from src.auth.config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate


router = APIRouter()


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    tags=["auth"],
)
