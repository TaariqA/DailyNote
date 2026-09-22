from backend.app.models.user import User
from sqlalchemy.orm import Session
from sqlalchemy import update
from backend.app.schemas.user import UserIn, NameUpdate
from fastapi import HTTPException
from backend.app.core.security import hash_user_password

def get_user_by_id(user_id:int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
            raise HTTPException(status_code=404, detail="User Not Found")
    
    return {"email": user.email, 
            "name": user.name,
            "user_id": user.id
    }

def add_new_user_to_db(user: UserIn, db: Session):
    #work on function to hash user password

    new_user = User(
                    email = user.email,
                    name = user.name,
                    password_hash = hash_user_password(user.password_hash)
                    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"email": new_user.email, 
            "name": new_user.name,
            "user_id": new_user.id
    }

def change_username(user_id: int, name_update: NameUpdate, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
           raise HTTPException(status_code=404, detail="User not found")

    edit = update(User).where(User.id == user_id).values(name = name_update.new_name)
    db.execute(edit)
    db.commit()
    db.refresh(user)

    return {
           "email": user.email,
           "name": user.name,
           "user_id": user.id
    }


    

