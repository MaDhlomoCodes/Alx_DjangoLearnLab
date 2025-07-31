from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic.detail import DetailView

# Home view
def home(request):
    return HttpResponse("Welcome to the Relationship App!")

# About view
def about(request):
    return HttpResponse("This is the About page of the Relationship App.")

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class-based view for a specific library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
