from sqlalchemy import Column, Integer, String, LargeBinary
from backend.app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column

#Model for the user table, contains id, email, password
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    password_hash: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)