from fastapi import Depends, APIRouter
from core.database.db import get_db
from sqlalchemy.orm import Session
from app.services import list_serv

list_router = APIRouter(tags=["List of Swiped Users"])

@list_router.get("/user-list")
async def user_list(uid:int, swipe:str, db:Session = Depends(get_db)):
    return list_serv(uid, swipe, db)


