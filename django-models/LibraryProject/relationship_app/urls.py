from django.urls import path
from .views import home, list_books, LibraryDetailView

urlpatterns = [
    path('', home, name='home'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
