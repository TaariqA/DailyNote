#MODULES TO CREATE ENGINE THAT CONNECTS TO DATABASE & CREATE A SESSION FOR ROUTES TO ACCESS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from backend.app.core.config import settings

#assigning .env secret to a variable
DB_LINK = settings.database_url

#error catching just in case DB_LINK doesnt exist
if not DB_LINK:
    raise ValueError("DB_LINK environment variable is not set")

#responsible for managing database data
engine = create_engine(DB_LINK, echo=True)

#Sessions for API to access engine & thus database (flush adds data to database non-permanantly, commit saves to database)
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
