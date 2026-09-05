from fastapi import APIRouter, Depends
from pydantic import BaseModel

from sqlalchemy.orm import Session
from app.db.session import get_db

router = APIRouter()

class FragranceIn(BaseModel):
    name: str
    brand: str
    top_notes: list[str]
    middle_notes: list[str]
    base_notes: list[str]
    season_rec: str
    timeofday_rec: str

class FragranceOut(BaseModel):
    name: str
    brand: str
    top_notes: list[str]
    middle_notes: list[str]
    base_notes: list[str]
    season_rec: str
    timeofday_rec: str
    frag_id: int

@router.get("/")
def health_check():
    return {"Fragrance routes": "Healthy!"}

@router.post("/fragrances", response_model=FragranceOut)
def new_fragrance(new_frag: FragranceIn, db: Session = Depends(get_db)):
    #return add_new_fragrance_to_database(new_frag, db)
    pass

@router.get("/fragrances/{frag_id}", response_model=FragranceOut)
def get_fragrance(frag_id: int, db: Session = Depends(get_db)):
    #return get_fragrance_by_id(frag_id, db)
    pass