from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserFragranceLink(BaseModel):
    user_id: int
    frag_id: int
    message: str = "linked"

@app.post("/users/{user_id}/fragrances/{frag_id}", response_model=UserFragranceLink)
def add_fragrance(user_id: int, frag_id: int):
    #join_user_to_frag(user_id, frag_id)
    pass
