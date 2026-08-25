#MODULES TO CREATE ENGINE THAT CONNECTS TO DATABASE & CREATE A SESSION FOR ROUTES TO ACCESS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
#MODULES TO ACCESS SECRETS IN .ENV
from dotenv import load_dotenv
import os

#assigning .env secret to a variable
load_dotenv()
DB_LINK = os.getenv("DB_LINK")

#error catching just in case DB_LINK doesnt exist
if not DB_LINK:
    raise ValueError("DB_LINK environment variable is not set")

#responsible for managing database data
engine = create_engine(DB_LINK, echo=True)

#Sessions for API to access engine & thus database
sessionLocal = sessionmaker(
    autoflush=False,
    bind=engine
)

#FASTAPI DB access
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
