from sqlalchemy import Column, Integer, String
from app.db.base import Base

#model for an individual note, no duplicate notes are allowed, columns: id, scent family, name
class Note(Base):
    __tablename__= "notes"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True, nullable=False)
    scent_family = Column(String, index=True, nullable=False)