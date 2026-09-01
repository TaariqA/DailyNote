from sqlalchemy import Column, Integer, String, JSON
from app.db.base import Base

#model for fragrances, each requires an id, name, & brand
class Fragrance(Base):
    __tablename__ = "fragrances"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    brand = Column(String, index=True, nullable=False)
    top_notes = Column(JSON, nullable = True)
    middle_notes = Column(JSON, nullable = True)
    base_notes = Column(JSON, nullable = True)
    season_rec = Column(String, nullable= True)
    timeofday_rec = Column(String, nullable= True)