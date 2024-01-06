from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'catalog/book_list.html', {'books': books})
