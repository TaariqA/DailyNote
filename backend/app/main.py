from fastapi import FastAPI
from backend.app.api.fragrance import router as fragrance_router
from backend.app.api.user import router as user_router
from backend.app.api.userfragcollection import router as userfragcollection_router
app = FastAPI()

app.include_router(fragrance_router)
app.include_router(user_router)
app.include_router(userfragcollection_router)