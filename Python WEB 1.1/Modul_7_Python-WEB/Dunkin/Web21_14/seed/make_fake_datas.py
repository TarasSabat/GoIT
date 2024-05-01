from random import randint

from faker import Faker
from sqlalchemy import select

from app.db_models import Client, Address, Goods, GoodsForClients
from app.db import session


fake = Faker(locale="uk-UA")


def make_fake_data():    
    for i in range(10):
        client = Client(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            addresses = [
                Address(
                    city = fake.city(), 
                    street = fake.street_name(), 
                    building = fake.building_number()
                    ) 
                for _ in range(randint(1, 3))
                ]
            )
        session.add(client)
    session.commit()
    

def make_fake_goods():
    goods_list = ["drink", "meat", "bread"]
    
    for goods in goods_list:
        session.add(Goods(name = goods))
    session.commit()
    
 
def make_goods_for_client():
    select_clients = select(Client)
    clients = session.scalars(select_clients)
    
    select_goods = select(Goods)
    goods = list(session.scalars(select_goods))
    
    for client in clients:
        gfc_list = [GoodsForClients(goods_id = g.id) for g in goods]
        client.goods_assoc.extend(gfc_list)
        session.commit()


if __name__ == '__main__':
    make_goods_for_client()