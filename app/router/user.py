from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database.db import get_db
from datetime import date
from app.services import user

user_router = APIRouter(tags=["User"])

@user_router.post('/user_registration')
async def user_create(name:str, DOB: date, gender: str, pref_gender : str, bio: str, db:Session = Depends(get_db)):
    return user.user_serv(name,DOB,gender,pref_gender,bio,db)

