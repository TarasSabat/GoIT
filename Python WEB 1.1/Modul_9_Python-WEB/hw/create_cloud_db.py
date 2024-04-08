import json
import pymongo
from mongoengine import disconnect

disconnect()


# Підключення до MongoDB Atlas
def connect_to_mongodb(uri):
    client = pymongo.MongoClient(uri)
    return client


# Завантаження даних з файлу JSON
def load_data_from_json(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


# Основна функція для створення та заповнення бази даних
def main():
    # Підключення до MongoDB Atlas
    mongodb_uri = (
        "mongodb+srv://goitlearn:1q2w3e4R@cluster0.kkkewau.mongodb.net/?retryWrites=true&w"
        "=majority"
        "&appName=Cluster0"
    )
    client = connect_to_mongodb(mongodb_uri)

    # Вибір бази даних та колекцій
    db = client["hw_8"]
    authors_collection = db["authors"]
    quotes_collection = db["quotes"]

    # Завантаження даних з файлів JSON
    authors_data = load_data_from_json("authors.json")
    quotes_data = load_data_from_json("quotes.json")

    # Вставка даних до колекції авторів
    authors_collection.insert_many(authors_data)

    # Вставка даних до колекції цитат
    quotes_collection.insert_many(quotes_data)

    print("Дані успішно завантажені до бази даних MongoDB Atlas.")


if __name__ == "__main__":
    main()
