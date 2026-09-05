from fastapi import APIRouter, Depends
from pydantic import BaseModel, EmailStr
from app.services.user_logic import get_user_by_id

from sqlalchemy.orm import Session
from app.db.session import get_db


router = APIRouter()

class UserIn(BaseModel):
    email: EmailStr
    name: str
    password_hash: str

class UserOut(BaseModel):
    email: EmailStr
    name: str
    user_id: int

class NameUpdate(BaseModel):
    new_name: str

@router.get("/")
def health_check():
    return {"User routes": "Healthy!"}

@router.get("/users/{user_id}",response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(user_id, db)

@router.post("/users", response_model=UserOut)
def create_user(user: UserIn, db: Session = Depends(get_db)):
    pass
    #return add_new_user_to_db(user, db)

@router.patch("/users/{user_id}", response_model=UserOut)
def update_user_name(user_id: int, name_update: NameUpdate, db: Session = Depends(get_db)):
    pass
    #return change_username(user_id, NameUpdate, db)

@router.delete("/users/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    pass
    #return delete_user_by_id(user_id, db)