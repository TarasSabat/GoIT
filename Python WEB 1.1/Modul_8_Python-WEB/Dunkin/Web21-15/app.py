from datetime import datetime
import os

from mongoengine import connect
from dotenv import load_dotenv

from models import Cat, Vaccine


load_dotenv()


MONGO_PASS = os.getenv("MONGO_PASS")
URI = f"mongodb+srv://vdunkin:{MONGO_PASS}@cluster0.vmj7irm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

connect(host=URI, db='MyCats')

cat = Cat(name='Sirko', color='Black', vaccines=[Vaccine(vaccine_date=datetime.now())]).save()