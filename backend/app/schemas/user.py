from pydantic import BaseModel, EmailStr

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
