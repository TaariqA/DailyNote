from sqlalchemy import Column, Integer, String, ForeignKey
from backend.app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class UserFragJoin(Base):
    __tablename__ = "user_frag_join"

    link_id: Mapped[int] = mapped_column(Integer, autoincrement= True, primary_key= True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False, index= True)
    frag_id: Mapped[int] = mapped_column(Integer, ForeignKey("fragrances.id"), nullable=False)