from bson.objectid import ObjectId
#todo
from django import template

from ..utils import get_mongodb

from quotes.models import Author #!

register = template.Library()

def get_author(author_id):
    try:
        author = Author.objects.get(id=author_id)
        return author
    except Author.DoesNotExist:
        return None


# def get_author(id_):
#     db = get_mongodb()
#     author = db.authors.find_one({"_id": ObjectId(id_)})
#     return author["fullname"]


register.filter("author", get_author)



