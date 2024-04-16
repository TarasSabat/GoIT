from django.contrib import admin
from django.urls import path, include
from users.views import registration_view, login_view, logout_view, add_author_view, add_quote_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("quotes.urls")),
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('add_author/', add_author_view, name='add_author'),
    path('add_quote/', add_quote_view, name='add_quote')
    # path("users/", include("users.urls")),
]
