from django.contrib import admin
from django.urls import path, include
from quotes import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("quotes.urls")),
    path("users/", include("users.urls")),
    # path('author_create/', views.author_create, name='author_create'),
]
