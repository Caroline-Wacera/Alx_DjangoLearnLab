from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'publication_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter publication year'}),
        }
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'publication_year': 'Publication Year',
        }
        help_texts = {
            'title': 'Enter the title of the book.',
            'author': 'Enter the name of the author.',
            'publication_year': 'Enter the year the book was published.',
        }
        error_messages = {
            'title': {
                'required': 'This field is required.',
            },
            'author': {
                'required': 'This field is required.',
            },
            'publication_year': {
                'required': 'This field is required.',
                'invalid': 'Enter a valid year.',
            },
        }
