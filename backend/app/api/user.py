from fastapi import APIRouter, Depends
from backend.app.services.user_logic import get_user_by_id, change_username, add_new_user_to_db
from backend.app.schemas.user import UserIn, UserOut, NameUpdate

from sqlalchemy.orm import Session
from backend.app.db.session import get_db


router = APIRouter()

@router.get("/")
def health_check():
    return {"User routes": "Healthy!"}

@router.get("/users/{user_id}",response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(user_id, db)

@router.post("/users", response_model=UserOut)
def create_user(user: UserIn, db: Session = Depends(get_db)):
    return add_new_user_to_db(user, db)

@router.patch("/users/{user_id}", response_model=UserOut)
def update_user_name(user_id: int, name_update: NameUpdate, db: Session = Depends(get_db)):
    pass
    return change_username(user_id, name_update, db)

@router.delete("/users/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    pass
    #return delete_user_by_id(user_id, db)