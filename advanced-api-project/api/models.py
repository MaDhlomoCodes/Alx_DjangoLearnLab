from django.db import models

class Author(models.Model):
    """
    Author model represents an author of books.
    """
    name = models.CharField(max_length=100)  # Author's full name

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a book with a title, publication year,
    and a foreign key relationship to an Author.
    """
    title = models.CharField(max_length=200)  # Title of the book
    publication_year = models.IntegerField()  # Year book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    # 'related_name' allows reverse querying author.books.all()

    def __str__(self):
        return self.title
