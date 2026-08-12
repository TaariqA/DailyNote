from sqlalchemy import Column, Integer, String
from app.db.base import Base

class FragranceNote(Base):
    __tablenote__ = "fragrance_notes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fragrance_id = 
    note_id = 
    pyramid_placement = 