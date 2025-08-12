from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Author model
    Supports list, create, retrieve, update, delete
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Book model
    Supports list, create, retrieve, update, delete
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
