from django.contrib import admin
from django.urls import path, include
from users import views  # add_author_view, add_quote_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("quotes.urls")),
    path("users/", include("users.urls")),
]
