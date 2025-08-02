from django import forms
from .models import Book
from django.contrib.auth import get_user_model
User = get_user_model()

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'  # list specific fields like ['title', 'author']
