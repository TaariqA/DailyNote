from pydantic import BaseModel

#longevity and sillage are based on the average of Fragrantica user ratings, 1 star through 5 stars
#Seasons will be the two highest voted seasons
#notes are a list of dicts including each fragrance's name and weight e.g. {"name": name, "weight": 10}
 
class Fragrance(BaseModel):
    id: int
    name: str
    brand: str
    gender: str
    description: str
    picture: str
    top_notes: list[dict]
    middle_notes: list[dict]
    base_notes: list[dict]
    notes_flat: list[dict]
    longevity: int
    sillage: int
    season: str