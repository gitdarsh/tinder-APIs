from fastapi import APIRouter

from .login import login_router
from .user import user_router
from .swipe import swipe_router
from .list import list_router

router = APIRouter()

router.include_router(login_router)
router.include_router(user_router)
router.include_router(swipe_router)
router.include_router(list_router)