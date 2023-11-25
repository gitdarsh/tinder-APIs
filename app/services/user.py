from datetime import date
from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException

def user_serv(name:str, DOB:date, gender:str, pref_gender:str, bio:str, db:Session):
    check_user = db.execute(text("SELECT uid FROM user_data WHERE name = :name AND DOB = :DOB AND gender = :gender AND pref_gender = :pref_gender"),
                                 {
                                     "name":name,
                                     "DOB":DOB,
                                     "gender":gender,
                                     "pref_gender":pref_gender
                                 }).fetchone()
    
    #This is not a good way to check unique users, using a join between user_data and phone table on id=uid will be better.
    if check_user:
        #add http exception
        raise HTTPException(status_code=400, detail="User already registered.")
    
    db.execute(text("INSERT INTO user_data (name,DOB,gender,pref_gender,bio) VALUES (:name,:DOB,:gender,:pref_gender,:bio)"),
                    {
                        "name":name,
                        "DOB":DOB,
                        "gender":gender,
                        "pref_gender":pref_gender,
                        "bio":bio
                    })
    db.commit()
    return {"Congrats! You are registered!"}