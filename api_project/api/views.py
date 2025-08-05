from rest_framework import generics
from .models import BookList 
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = BookList.objects.all()
    serializer_class = BookSerializer