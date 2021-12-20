from fastapi import APIRouter
from app.router import animal, tools, db

API_PREFIX = "/api"

router = APIRouter()
router.include_router(animal.router, tags=["animal"], prefix=API_PREFIX + "/animal")
router.include_router(tools.router, tags=["tools"], prefix=API_PREFIX + "/tools")
router.include_router(db.router, tags=["user"], prefix=API_PREFIX + "/user")
