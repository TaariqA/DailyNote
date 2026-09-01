from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class UserFragJoin(Base):
    __tablename__ = "user_frag_join"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    frag_id = Column(Integer, ForeignKey("fragrances.id"), nullable=False)