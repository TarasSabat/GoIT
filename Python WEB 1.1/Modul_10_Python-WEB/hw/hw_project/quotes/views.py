from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Author, Quote
from .utils import get_mongodb


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


def author_create(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname', '')
        born_date = request.POST.get('born_date', '')
        born_location = request.POST.get('born_location', '')
        description = request.POST.get('description', '')
        quote_text = request.POST.get('quote', '')

        # Створення автора
        author = Author(fullname=fullname, born_date=born_date, born_location=born_location, description=description)
        author.save()

        # Створення цитати та збереження її з автором
        quote = Quote(quote=quote_text, author=author)
        quote.save()

        if request.method == 'POST':
            print(request.POST)

        return redirect('quotes:root')  # Перенаправлення на сторінку зі списком авторів
    return render(request, 'quotes/author_create.html')