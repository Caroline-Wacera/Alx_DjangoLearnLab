from django.urls import path
from .views import home, list_books, LibraryDetailView  # Import views

urlpatterns = [
    path('', home, name='home'),  # Homepage route
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]
