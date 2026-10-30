from backend.app.models.user import User
from sqlalchemy.orm import Session
from sqlalchemy import update, select
from backend.app.schemas.user import UserIn, NameUpdate
from fastapi import HTTPException
from backend.app.core.security import password_hash

def get_user_by_id(user_id:int, db: Session) -> User:
    user = db.get(User, user_id)

    if not user:
            raise HTTPException(status_code=404, detail="User Not Found")
    
    return user

def get_user_by_email(email:str, db: Session, ) -> User:
    user = db.scalar(select(User).where(User.email == email))

    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    
    return user 
    

def add_new_user_to_db(user: UserIn, db: Session) -> User:
    #work on function to hash user password

    new_user = User(
                    email = user.email,
                    name = user.name,
                    password_hash = password_hash(user.password)
                    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return db.get(User, new_user.id)

def change_username(user_id: int, name_update: NameUpdate, db: Session):
    user = db.get(User, user_id)

    if not user:
           raise HTTPException(status_code=404, detail="User not found")

    user.name = name_update.new_name
    db.commit
    db.refresh(user)

    return user


    

