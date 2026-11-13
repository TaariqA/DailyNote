from fastapi import APIRouter, Depends, HTTPException
from backend.app.services.user_logic import get_user_by_id, change_username, add_new_user_to_db
from backend.app.schemas.user import UserIn, UserOut, NameUpdate, LoginRequest, Token
from backend.app.core.security import authenticate_user, create_access_token

from sqlalchemy.orm import Session
from backend.app.db.session import get_db


router = APIRouter()

@router.get("/")
def health_check():
    return {"User routes": "Healthy!"}

@router.get("/users/{user_id}",response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(user_id, db)

@router.post("/login", response_model=Token)
async def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(credentials.email, credentials.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", status_code=201, summary="Create a new user")
def create_user(user: UserIn, db: Session = Depends(get_db)):
    add_new_user_to_db(user, db)
    return {"message": "User registered successfully"}

@router.patch("/users/{user_id}", response_model=UserOut)
def update_user_name(user_id: int, name_update: NameUpdate, db: Session = Depends(get_db)):
    pass
    return change_username(user_id, name_update, db)

@router.delete("/users/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    pass
    #return delete_user_by_id(user_id, db)