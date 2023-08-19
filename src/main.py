from fastapi import FastAPI

from src.auth.routers import router as users_router
from src.garden.routers import router as garden_router

app = FastAPI()


app.include_router(
    garden_router,
    prefix="/gardens",
    tags=["Garden"]
)


app.include_router(
    users_router,
    prefix="/users",
    tags=["User"]
)
