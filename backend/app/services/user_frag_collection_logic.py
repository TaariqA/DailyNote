from sqlalchemy.orm import Session
from backend.app.models.userfragcollection import UserFragJoin
from backend.app.schemas.userfragcollection import UserFragranceLinkDelete, UserFragranceLink, UserFragranceEntry
from fastapi import HTTPException

def join_user_to_frag(entered_link: UserFragranceEntry, db: Session) -> UserFragranceLink:
    join = UserFragJoin(
        frag_id = entered_link.frag_id,
        user_id = entered_link.user_id
    )
    db.add(join)
    db.commit()
    return join

def remove_user_fragrance_join(link_id:int, db:Session) -> UserFragranceLinkDelete:
    link_to_delete = db.get(UserFragJoin, link_id)

    db.delete(link_to_delete)
    db.commit()
    return link_to_delete