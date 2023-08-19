import datetime

from pydantic import BaseModel, Field


class GardenCreate(BaseModel):
    name: str
    size: int = Field(gt=0)


class GardenList(BaseModel):
    id: int
    name: str
    size: int
    user_id: int
