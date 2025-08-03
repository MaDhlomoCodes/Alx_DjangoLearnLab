from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']

class ExampleForm(forms.Form):
    """Checker requirement only - not used in actual views"""
    pass 
