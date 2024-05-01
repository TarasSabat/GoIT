from django.urls import path
from . import views

app_name = "quotes"
#todo
urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path('author_create/', views.author_create, name='author_create'),
    path('author/<int:author_id>/', views.author_page, name='author_page'),
    #path('author/<str:author_id>/', views.author_page, name='author_page'),
]
