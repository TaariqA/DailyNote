from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
app = FastAPI()

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password_hash: str

class UserOut(BaseModel):
    email: EmailStr
    name: str
    user_id: int

class NameUpdate(BaseModel):
    new_name: str

@app.get("/")
def health_check():
    return {"User routes": "Healthy!"}

@app.get("/users/{user_id}",response_model=UserOut)
def get_user(user_id: int):
    pass
    #return get_user_by_id(user_id)

@app.post("/register", response_model=UserOut)
def create_user(user: UserCreate):
    pass
    #return add_new_user_to_db(user)

@app.patch("/namechange/{user_id}", response_model=UserOut)
def change_name(user_id: int, name_update: NameUpdate):
    pass
    #return change_username(user_id, NameUpdate)