from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session 

from ex01_simple_usage import BD_URL, Vehicle, Model


engine = create_engine(BD_URL)

with Session(engine) as session:
    # select_query = select(Vehicle).where(Vehicle.id == 2)
    
    # vehicle = session.scalar(select_query)
    
    # vehicle.color = "green"

    # session.commit()    
    
    # select_query = select(Vehicle).where(Vehicle.id == 2)
    
    # vehicle = session.scalar(select_query)
    
    # print(vehicle)
    
    query = select(Vehicle)
    
    for v in session.scalars(query):
        v.color = "purple"
        
    # new_vehicle = Vehicle(brand="IVECO", models = [Model(model_name="Turbo daily")])
    
    # session.add(new_vehicle)
    
    session.commit()