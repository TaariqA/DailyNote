from app.models.user import User
from sqlalchemy.orm import Session

from app.api.user import UserIn

def get_user_by_id(user_id:int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return{"error": "user not found"}
    
    return {"email": user.id, 
            "name": user.email,
            "id": user.name
            }

def add_new_user_to_db(user: UserIn, db: Session):
    #work on function to hash user password

    new_user = {"email": user.email,
                "name": user.name,
                "password": ""#hashed password
                }
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user