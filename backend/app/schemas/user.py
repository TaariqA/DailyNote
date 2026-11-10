from pydantic import BaseModel, EmailStr, ConfigDict, Field

class UserIn(BaseModel):
    email: EmailStr
    name: str
    password: str

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: EmailStr
    name: str
    user_id: int = Field(validation_alias = "id")

class NameUpdate(BaseModel):
    new_name: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
