from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
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
def get_user(user_id: int):
    pass
    #return get_user_by_id(user_id)

@router.post("/users", response_model=UserOut)
def create_user(user: UserIn):
    pass
    #return add_new_user_to_db(user)

@router.patch("/users/{user_id}", response_model=UserOut)
def update_user_name(user_id: int, name_update: NameUpdate):
    pass
    #return change_username(user_id, NameUpdate)

@router.delete("/users/delete/{user_id}")
def delete_user(user_id: int):
    pass
    #return delete_user_by_id(user_id)