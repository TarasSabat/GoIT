from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Author, Quote
#TODO
# from .utils import get_mongodb




#TODO
def main(request):
    page_number = request.GET.get('page', 1)
    quotes = Quote.objects.all().order_by('-created_at')  # Отримання всіх цитат із бази даних SQLite # db =
    per_page = 10
    paginator = Paginator(quotes, per_page)  #paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.get_page(page_number)
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
#TODO
        # if request.method == 'POST':
        #     print(request.POST)

        return redirect('quotes:root')  # Перенаправлення на сторінку зі списком авторів
    return render(request, 'quotes/author_create.html')

 # TODO
def author_page(request, author_id):
   # Отримати об'єкт автора за його ідентифікатором
    author = Author.objects.get(id=author_id)
    #return render(request, 'quotes/author_page.html', {'author_id': author_id})
    return render(request, 'quotes/author_page.html', {'author': author_id})