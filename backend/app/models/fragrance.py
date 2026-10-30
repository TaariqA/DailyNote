from sqlalchemy import Column, Integer, String, JSON
from backend.app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column

#model for fragrances, each requires an id, name, & brand

class Note():
    name: str
    weight: int

class Fragrance(Base):
    __tablename__ = "fragrances"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, index=True, nullable= False)
    brand: Mapped[str] = mapped_column(String, index=True, nullable= False)
    top_notes: Mapped[list[Note]] = mapped_column(JSON, nullable = False)
    middle_notes: Mapped[list[Note]] = mapped_column(JSON, nullable = False)
    base_notes: Mapped[list[Note]] = mapped_column(JSON, nullable = False)
    season_rec: Mapped[str] = mapped_column(String, nullable= False)
    timeofday_rec: Mapped[str] = mapped_column(String, nullable= False)