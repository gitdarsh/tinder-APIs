from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException

def login_serv(Phone:int,db:Session):
    existing_number = db.execute(text("SELECT id FROM phone where number = :Phone"),
                                 {
                                     'Phone':Phone
                                 }).fetchone()
    if existing_number:
        return {"Phone Number already exists."}
    else:
        db.execute(text("INSERT INTO phone (number) VALUES (:Phone)"),
                {
                    'Phone':Phone
                })
        db.commit()
        return {"Phone Number added."}
#add http exception
