from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class FragranceIn(BaseModel):
    name: str
    brand: str

class FragranceOut(BaseModel):
    name: str
    brand: str
    frag_id: int

@app.get("/")
def health_check():
    return {"Fragrance routes": "Healthy!"}

@app.post("/fragrances", response_model=FragranceOut)
def new_fragrance(new_frag: FragranceIn):
    #return add_new_fragrance_to_database(new_frag)
    pass
    

@app.get("/fragrances/{frag_id}", response_model=FragranceOut)
def get_fragrance(frag_id: int):
    #return get_fragrance_by_id(frag_id)
    pass