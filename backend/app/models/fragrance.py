from sqlalchemy import Integer, String, JSON
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.db.base import Base
#model for fragrances, each requires an id, name, & brand

class Fragrance(Base):
    __tablename__ = "fragrances"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    slug: Mapped[str] = mapped_column(String, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    brand: Mapped[str] = mapped_column(String, nullable=False)
    gender: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    picture: Mapped[str] = mapped_column(String, nullable=False)
    top_notes: Mapped[list[dict]] = mapped_column(JSON, nullable=True)
    middle_notes: Mapped[list[dict]] = mapped_column(JSON, nullable=True)
    base_notes: Mapped[list[dict]] = mapped_column(JSON, nullable=True)
    notes_flat: Mapped[list[dict]] = mapped_column(JSON, nullable=True)
    longevity: Mapped[int] = mapped_column(Integer, nullable=False)
    sillage: Mapped[int] = mapped_column(Integer, nullable = False)
    season: Mapped[str] = mapped_column(String, nullable = False)


