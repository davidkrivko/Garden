import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.config import current_user
from src.garden.models import Garden
from src.auth.models import User
from src.database import get_async_session
from src.garden.schemas import GardenCreate

router = APIRouter()


@router.get("/")
async def get_gardens(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    query = select(Garden).filter(Garden.user_id == user.id)
    result = await session.execute(query)

    return result.scalars().all()


@router.post("/")
async def create_garden(
        garden: GardenCreate,
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session)
):
    now = datetime.datetime.now()

    garden = Garden(
        name=garden.name,
        size=garden.size,
        created_at=now,
        user_id=user.id,
    )

    session.add(garden)
    await session.commit()

    return {
        "status": 201,
        "data": garden,
        "detail": "Garden was successfully created!"
    }
