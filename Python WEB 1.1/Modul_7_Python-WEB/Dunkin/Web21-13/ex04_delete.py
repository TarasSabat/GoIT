from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session 

from ex01_simple_usage import BD_URL, Vehicle, Model


engine = create_engine(BD_URL)

with Session(engine) as session:
    vehicle = session.get(Vehicle, 14)
    session.delete(vehicle)
    session.commit()