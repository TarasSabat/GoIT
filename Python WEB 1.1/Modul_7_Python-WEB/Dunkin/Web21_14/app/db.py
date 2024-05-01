from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, declarative_base


class Base(DeclarativeBase):
    pass

# Base = declarative_base()

DB_URL = "postgresql://postgres:postgres@localhost/test_alembic"

engine = create_engine(DB_URL)

DBSession = sessionmaker(bind=engine)
session = DBSession()