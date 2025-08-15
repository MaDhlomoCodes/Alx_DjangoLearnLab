from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client = APIClient()

        # Create an author
        self.author = Author.objects.create(name="Author One")

        # Create a book
        self.book = Book.objects.create(
            title="Book One",
            author=self.author,
            publication_year=2024
        )

        # Endpoints
        self.list_url = reverse("book-list")   # DRF router will give book-list & book-detail names
        self.detail_url = reverse("book-detail", args=[self.book.id])

    def test_list_books(self):
        """Test GET all books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_book_authenticated(self):
        """Test creating a book requires authentication"""
        self.client.login(username="testuser", password="testpass123")
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2025
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """Test unauthenticated users cannot create books"""
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2025
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        """Test updating a book"""
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "Updated Book", "author": self.author.id, "publication_year": 2025}
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book_authenticated(self):
        """Test deleting a book"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        """Test filtering books by title"""
        response = self.client.get(self.list_url, {"title": "Book One"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_order_books(self):
        """Test ordering books by publication_year"""
        Book.objects.create(title="Older Book", author=self.author, publication_year=1999)
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))

    def test_search_books(self):
        """Test searching books by title"""
        response = self.client.get(self.list_url, {"search": "Book"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
