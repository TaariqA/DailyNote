from pydantic import BaseModel

class UserFragranceLink(BaseModel):
    user_id: int
    frag_id: int
    message: str = "linked"