from sqlalchemy import Column, Integer, String
from app.db.base import Base

#model for fragrances, each requires an id, name, & brand
class Fragrance(Base):
    __tablename__ = "fragrances"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    brand = Column(String, index=True, nullable=False)