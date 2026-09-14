from fastapi import APIRouter, Depends
from app.schemas.fragrance import FragranceIn, FragranceOut

from sqlalchemy.orm import Session
from app.db.session import get_db

router = APIRouter()

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