from bson.objectid import ObjectId
# todo
from django import template
from ..utils import get_mongodb
from ..models import Author  # !

register = template.Library()


def get_author(author_id):
    try:
        author = Author.objects.get(id=author_id)
        return author
    except Author.DoesNotExist:
        return None


register.filter("author", get_author)
