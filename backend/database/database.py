from typing import Iterator

from sqlalchemy import QueuePool, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from core.config import POSTGRES_DB_URL

Base = declarative_base()

engine = create_engine(
    POSTGRES_DB_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=5,
    pool_timeout=60,
    pool_recycle=1800,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_pg_db() -> Iterator[Session]:
    """FastAPI dependency that provides a sqlalchemy session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()