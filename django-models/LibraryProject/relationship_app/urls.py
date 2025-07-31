from .views import home
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('', home, name='home'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
