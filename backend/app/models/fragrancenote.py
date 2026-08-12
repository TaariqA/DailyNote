from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

#model for fragrance note table. Joins fragrance & note tables so that each 
class FragranceNote(Base):
    __tablenote__ = "fragrance_notes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fragrance_id = Column(Integer, ForeignKey("fragrances.id"), nullable=False)
    note_id = Column(Integer, ForeignKey("notes.id"), nullable=False)
    pyramid_placement = Column(String, nullable=False)