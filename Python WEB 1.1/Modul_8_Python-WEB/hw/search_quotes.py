from mongoengine import connect, disconnect
from models import Quote, Author

disconnect()
# Підключення до MongoDB Atlas
connect(
    host="mongodb+srv://goitlearn:1q2w3e4R@cluster0.kkkewau.mongodb.net/?retryWrites=true&w"
    "=majority"
    "&appName=Cluster0"
)


def search_quotes_by_author(author_name):
    author = Author.objects(fullname=author_name).first()
    if author:
        quotes = Quote.objects(author=author)
        return print_quotes(quotes)
    else:
        return []


def search_quotes_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    return print_quotes(quotes)


def search_quotes_by_tags(tags):
    tags_list = tags.split(",")
    quotes = Quote.objects(tags__in=tags_list)
    return print_quotes(quotes)


def print_quotes(quotes):
    unique_quotes = set(quote.quote for quote in quotes)
    for quote in unique_quotes:
        print(quote)


def main():
    while True:
        command = input("Введіть команду: ").strip()

        if command.startswith("name:"):
            author_name = command.split(":")[1].strip()
            search_quotes_by_author(author_name)
        elif command.startswith("tag:"):
            tag = command.split(":")[1].strip()
            search_quotes_by_tag(tag)
        elif command.startswith("tags:"):
            tags = command.split(":")[1].strip()
            search_quotes_by_tags(tags)
        elif command == "exit":
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
