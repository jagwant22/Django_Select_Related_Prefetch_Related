from django.shortcuts import render, HttpResponse
from .models import Book, Publisher, Store
import json
from django.http import JsonResponse
def home(request):
	return HttpResponse("Hello")

def get_book_listing(request):
	book_list = list()
	queryset = Book.objects.all()

	for book in queryset :
		book_list.append({
			'id' :book.id, 'name':book.name, 'publisher': book.publisher.name
			})

	return JsonResponse(book_list, safe=False)

def get_book_listing_better(request):
	queryset = Book.objects.select_related('publisher').all()

	books = []
	for book in queryset : 
		books.append({'id' : book.id, 'name': book.name, 'publisher' : book.publisher.name})

	return JsonResponse(books, safe=False)

def get_store_listing(request):
	queryset = Store.objects.all()
	stores = []

	for store in queryset:
		books = [str(book) for book in store.books.all()]
		stores.append({'id': store.id, 'name':store.name, 'books':books})

	return JsonResponse(stores, safe=False)

def get_stores_quickly(request):
	queryset = Store.objects.prefetch_related('books')

	stores = []

	for store in queryset:
		books = [str(book) for book in store.books.all()]
		stores.append({'id':store.id, 'name':store.name, 'books':books})

	return JsonResponse(stores, safe=False)