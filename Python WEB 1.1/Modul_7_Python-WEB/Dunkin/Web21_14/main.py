from seed.make_fake_datas import make_fake_data, make_fake_goods, make_goods_for_client



if __name__ == '__main__':
    
    # Base.metadata.create_all(bind=engine)
    
    # stmt = select(Client).where(Client.id == 1)

    # result = session.scalars(stmt)
    
    # for client in result:
    #    for assoc in client.goods_assoc:
    #        print(assoc.goods_id)
    make_fake_data()
    make_fake_goods()
    make_goods_for_client()