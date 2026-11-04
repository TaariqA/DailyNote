from pydantic import BaseModel

class UserFragranceEntry(BaseModel):
    frag_id: int
    user_id: int

class UserFragranceLink(BaseModel):
    link_id: int
    user_id: int
    frag_id: int
    message: str = "linked"

class UserFragranceLinkDelete(BaseModel):
    link_id: int
    user_id: int
    frag_id: int
    message: str = "link Deleted"