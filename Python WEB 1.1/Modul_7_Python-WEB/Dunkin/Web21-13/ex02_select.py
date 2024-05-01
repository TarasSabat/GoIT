from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session 

from ex01_simple_usage import BD_URL, Vehicle, Model



engine = create_engine(BD_URL)

with Session(engine) as session:
    select_query = select(Model).where(Model.vehicle_id == 0)
    
    print(select_query)
    
    # for m in session.scalars(select_query):
    #     print(type(m.vehicle))
    print(len(list(session.scalars(select_query))))
    result = session.scalar(select_query)
    
    if result:
        ... # do
    