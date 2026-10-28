from sqlalchemy import Column, Integer, String, ForeignKey
from backend.app.db.base import Base

class UserFragJoin(Base):
    __tablename__ = "user_frag_join"

    link_id = Column(Integer, autoincrement= True, primary_key= True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index= True)
    frag_id = Column(Integer, ForeignKey("fragrances.id"), nullable=False)