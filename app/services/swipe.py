from sqlalchemy import text
from sqlalchemy.orm import Session

last_uid = None  # Variable to store the last UID

class Swipe:
    # def __init__(self) -> None:
    #     last_uid is None
    def swipe_left(swiper_id: int, swiped_id: int, db: Session):
            
            db.execute(text("INSERT INTO swipes(swiper_id,swiped_id,direction) VALUES (:swiper_id,:swiped_id,direction)"),
                       {
                            "swiper_id":swiper_id,
                            "swiped_id":swiped_id,
                            "direction":0
                       })
            db.commit()
            result = db.execute(text("SELECT uid, name FROM user_data WHERE uid > :swiped_id ORDER BY uid LIMIT 1"),
                                {"swiped_id": swiped_id}).fetchone()
            if result:
                # last_uid = result[0]  # Update last_uid with the new UID
                uid, name = result
                return {
                    "uid": uid,
                    "name": name
                }
            else:
                return {"You've run out of people to Swipe"}
            
    def swipe_right(swiper_id:int, swiped_id:int, db:Session):

        match = db.execute(text("SELECT swipe_id FROM swipes WHERE swiper_id=:swiped_id AND swiped_id=:swiper_id"),
                           {
                                "swiped_id":swiped_id,
                                "swiper_id":swiper_id
                           }).fetchone()
        
        if match:
            db.execute(text("INSERT INTO matches(user1,user2)VALUES(:swiper_id,:swiped_id)"),
                       {
                            "swiper_id":swiper_id,
                            "swiped_id":swiped_id
                       })
            db.commit()
            return {"Congrats! You two have matched!"}
        else:
            db.execute(text("INSERT INTO swipes(swiper_id,swiped_id,direction)VALUES(:swiper_id,:swiped_id,:direction)"),
                    {
                            "swiper_id":swiper_id,
                            "swiped_id":swiped_id,
                            "direction":1
                    })
            db.commit()
            result = db.execute(
            text("SELECT uid, name, DOB, gender, pref_gender, bio FROM user_data WHERE uid = :swiped_id"),
                {
                    "swiped_id": swiped_id
                }).fetchone()

            uid, name, DOB, gender, pref_gender, bio = result

            if result:
                return{
                    "uid":uid,
                    "name":name,
                    "DOB":DOB,
                    "gender":gender,
                    "pref_gender":pref_gender,
                    "bio":bio
                }
            else:
                return {"Sorry, no data found!"}
             
