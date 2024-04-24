from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Author
from .utils import get_mongodb


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


# def author_detail(request, author_id):
#     author = get_object_or_404(Author, id=author_id)
#     return render(request, 'quotes/author_detail.html', context={'author': author})
