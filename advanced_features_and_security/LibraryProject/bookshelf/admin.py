from django.contrib import admin
from .models import Book, CustomUser, CustomUserManager

admin.site.register(CustomUser, CustomUserAdmin)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Display fields in the admin list view
    search_fields = ("title", "author")  # Allow search by title and author
    list_filter = ("publication_year",)  # Add filter by publication year