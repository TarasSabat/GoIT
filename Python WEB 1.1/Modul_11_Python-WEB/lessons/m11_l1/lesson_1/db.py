from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = \
    "postgresql+psycopg2://root:changeme@localhost:5432/fast_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String(250))
    done = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
