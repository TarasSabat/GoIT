import sqlite3


insert_query = "INSERT INTO jobs(id) VALUES(6)"
update_query = "UPDATE jobs SET id=2 WHERE id=1"

select_query = "SELECT * FROM jobs WHERE id=5"


with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()
    
    cursor.execute(select_query)
    
    print(cursor.fetchone())

# conn = sqlite3.connect("example.db")

# cursor = conn.cursor()

# cursor.execute(insert_query)

# conn.commit()
# conn.close()

