from fastapi import APIRouter, Depends
from backend.app.schemas.userfragcollection import UserFragranceEntry, UserFragranceLink, UserFragranceLinkDelete
from backend.app.services.user_frag_collection_logic import remove_user_fragrance_join, join_user_to_frag, retrieve_user_fragrance_join

from sqlalchemy.orm import Session
from backend.app.db.session import get_db

router = APIRouter()

#NEEDS PROTECTION (MAKE SURE YOU CAN ONLY JOIN TO YOUR OWN ID)
@router.post("/users/{user_id}/fragrances/{frag_id}", response_model=UserFragranceLink)
def add_fragrance_link(link_entry: UserFragranceEntry, db: Session = Depends(get_db)):
    return join_user_to_frag(link_entry, db)

#NEEDS PROTECTION (MAKE SURE YOU CAN ONLY REMOVE JOIN PAIRED WITH YOUR ID)
@router.delete("/users/{user_id}/fragrances/{frag_id}", response_model=UserFragranceLinkDelete)
def delete_fragrance_link(link_id: int, db: Session = Depends(get_db)):
    return remove_user_fragrance_join(link_id, db)

#NEEDS PROTECTION (MAKE SURE YOU CAN ONLY RETRIEVE YOUR OWN FRAGRANCES)
@router.get("/users/{user_id}/fragrances")
def retrieve_user_fragrance_collection(user_id: int, db:Session = Depends(get_db)):
    return retrieve_user_fragrance_join(user_id, db)
