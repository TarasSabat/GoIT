import sqlite3


class DatabaseQuery:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, parameters=None):
        if parameters:
            self.cursor.execute(query, parameters)
        else:
            self.cursor.execute(query)
        results = self.cursor.fetchall()
        for row in results:
            print(row)

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


def main():
    request_number = int(input("Enter the request number >>> "))
    query_file = f"query_{request_number}.sql"

    db = DatabaseQuery("DZ_Mod_6.db")

    if request_number in [3, 5]:
        parameter = input("Enter the parameter value >>> ")

    with open(query_file, "r") as file:
        query = file.read()

    db.execute_query(query, (parameter,) if request_number in [3, 5] else None)
    db.close_connection()


if __name__ == "__main__":
    main()
