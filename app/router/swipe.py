from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from core.database.db import get_db
from app.services import Swipe

swipe_router = APIRouter(tags=["Swipe"])

@swipe_router.get('/swipe_left')
async def swipe_left_func(swiper_id: int, swiped_id:str, db:Session = Depends(get_db)):
    return Swipe.swipe_left(swiper_id, swiped_id, db)

@swipe_router.get('/swipe_right')
async def swipe_right(swiper_id:int, swiped_id:int, db:Session = Depends(get_db)):
    return Swipe.swipe_right(swiper_id, swiped_id, db)