from sys import path
from django.views.generic.detail import BaseDetailView
from django.views.generic.edit import BaseCreateView, BaseDeleteView, BaseUpdateView
from django.views.generic.list import BaseListView


urlpatterns = [
    path('books/', BaseListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BaseDetailView.as_view(), name='book-detail'),
    path('books/create/', BaseCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BaseUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BaseDeleteView.as_view(), name='book-delete'),
    path('books/update/', BaseUpdateView.as_view(), name='book-update-no-pk'),
    path('books/delete/', BaseDeleteView.as_view(), name='book-delete-no-pk'),
]
