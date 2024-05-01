from faker import Faker

from connection import create_connection, dsn_str


Faker.seed(1150)
fake_data = Faker(locale="uk-UA")

COUNTER = 100


# print(fake_data.name())
def insert_data(connection, sql_query):
    cursor = connection.cursor()
    
    cursor.executemany(sql_query, [(fake_data.name().split(" "))[:2] for _ in range(COUNTER)])
    connection.commit()
    

if __name__ == "__main__":
    sql_query = """
    INSERT INTO actor(first_name, last_name)
    VALUES (%s, %s)
    """
    with create_connection(dsn_str) as conn:
        insert_data(conn, sql_query)
    # print([(fake_data.name().split(" ")) for _ in range(COUNTER)])