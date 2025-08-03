from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'relationship'

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.list_books, name='list_books'),              # Changed from books/
    path('collections/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Changed from library/

    # Book CRUD with new paths
    path('catalog/add/', views.add_book, name='add_book'),
    path('catalog/<int:pk>/update/', views.edit_book, name='edit_book'),  # Changed from edit/
    path('catalog/<int:pk>/remove/', views.delete_book, name='delete_book'),  # Changed from delete/

    # Authentication URLs (unchanged)
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Role-Based Views (unchanged)
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]