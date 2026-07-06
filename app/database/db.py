from sqlalchemy.orm import declarative_base 
from sqlalchemy.orm import sessionmaker , Session
from sqlalchemy import create_engine
from app.config.app_config import get_app_config
from typing import Generator

Base = declarative_base()


config = get_app_config()

engine = create_engine(config.database_url)

SessionLocal = sessionmaker(autocommit=False , autoflush=False , bind=engine)
def get_db() -> Generator[Session, None , None]:
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

