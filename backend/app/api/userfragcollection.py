from fastapi import APIRouter, Depends
from app.schemas.userfragcollection import UserFragranceLink

from sqlalchemy.orm import Session
from app.db.session import get_db

router = APIRouter()

@router.post("/users/{user_id}/fragrances/{frag_id}", response_model=UserFragranceLink)
def add_fragrance(user_id: int, frag_id: int, db: Session = Depends(get_db)):
    #join_user_to_frag(user_id, frag_id, db)
    pass
