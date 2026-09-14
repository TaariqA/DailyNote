from pydantic import BaseModel

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