from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path('tag/<int:tag_id>/', views.quote_page, name='quote_page'),
    path('author_create/', views.author_create, name='author_create'),
    path('author/<int:author_id>/', views.author_page, name='author_page'),
]
