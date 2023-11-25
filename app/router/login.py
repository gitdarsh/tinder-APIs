from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database.db import get_db
from fastapi.exceptions import HTTPException
from app.services import login

login_router = APIRouter(tags=['login'])

@login_router.post('/login')
async def login_check(Phone:int,db:Session = Depends(get_db)):
    return login.login_serv(Phone,db)