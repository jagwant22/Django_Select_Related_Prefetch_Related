from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home),
    path("get_books", views.get_book_listing),
    path("get_books_quickly", views.get_book_listing_better),
    path('get_stores', views.get_store_listing),
    path('get_stores_quickly', views.get_stores_quickly)
]