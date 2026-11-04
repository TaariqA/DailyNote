from sqlalchemy import Column, Integer, String, JSON
from backend.app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column

#model for fragrances, each requires an id, name, & brand
class Fragrance(Base):
    __tablename__ = "fragrances"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    brand: Mapped[str] = mapped_column(String, index=True, nullable=False)
    top_notes: Mapped[JSON] = mapped_column(JSON, nullable = True)
    middle_notes: Mapped[JSON] = mapped_column(JSON, nullable = True)
    base_notes: Mapped[JSON] = mapped_column(JSON, nullable = True)
    season_rec: Mapped[str] = mapped_column(String, nullable= True)
    timeofday_rec: Mapped[str] = mapped_column(String, nullable= True)