from django import forms
from .models import Book


class BookAddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'category', 'cover', 'pdf')
