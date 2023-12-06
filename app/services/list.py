from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException

def list_serv(uid: int, swipe: str, db: Session):
    if swipe == "left":
        query = text("SELECT * FROM swipes WHERE swiper_id = :uid")
        result = db.execute(query, {"uid": uid}).fetchone()

        print("Query:", query)
        print("Result:", result)

        # Check if a result is           found
        if result is not None:
            # Convert the result to a dictionary
            result_dict = dict(result)
            return result_dict
        else:
            # Modify the message to indicate that records were found but not returned
            raise HTTPException(status_code=404, detail="Records found but not returned")
