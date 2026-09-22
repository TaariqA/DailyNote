from pydantic import BaseModel

class UserFragranceLink(BaseModel):
    link_id: int
    user_id: int
    frag_id: int
    message: str = "linked"