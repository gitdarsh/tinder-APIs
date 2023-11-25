# from sqlalchemy.ext import asyncio
from sqlalchemy import create_engine
from sqlalchemy.orm import(
    Session,
    sessionmaker,
    declarative_base
)

from core.config import config

# engine = asyncio.create_async_engine(
engine = create_engine(
    config.DB_URL,
    echo = False,
    pool_pre_ping = True
)

SessionLocal = sessionmaker(bind=engine, autocommit = False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()