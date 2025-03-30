from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

# Homepage View
def home(request):
    return HttpResponse("<h1>Welcome to the Library</h1><p>Go to <a href='/books/'>Books</a> to see all books.</p>")

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})  # Removed 'relationship_app/' prefix for template

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Removed 'relationship_app/' prefix for template
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Fetch all books in the library
        return context