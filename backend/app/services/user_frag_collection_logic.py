from sqlalchemy.orm import Session
from sqlalchemy import select

from fastapi import HTTPException

from backend.app.models.userfragcollection import UserFragJoin
from backend.app.schemas.userfragcollection import UserFragranceLinkDelete, UserFragranceLink, UserFragranceEntry
from backend.app.models.fragrance import Fragrance
from backend.app.models.user import User

#adds a user/fragrance link to join table
def join_user_to_frag(entered_link: UserFragranceEntry, db: Session) -> UserFragranceLink:
    join = UserFragJoin(
        frag_id = entered_link.frag_id,
        user_id = entered_link.user_id
    )
    db.add(join)
    db.commit()
    return join

#removes a link from the join table by link id
def remove_user_fragrance_join(link_id: int, db: Session) -> UserFragranceLinkDelete:
    link_to_delete = db.get(UserFragJoin, link_id)

    db.delete(link_to_delete)
    db.commit()
    return link_to_delete

#returned all fragrances owned by a user
def retrieve_user_fragrance_join(user_id: int, db: Session) -> list[Fragrance]:
    if db.get(User, user_id) is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    
    statement = select(Fragrance).join(UserFragJoin, UserFragJoin.frag_id == Fragrance.id).where(UserFragJoin.user_id == user_id).distinct()
    return list(db.scalars(statement).all())