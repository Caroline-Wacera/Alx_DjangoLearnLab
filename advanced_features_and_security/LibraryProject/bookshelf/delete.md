# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete it
book.delete()

# Confirm deletion
print(Book.objects.all())  # Should return an empty queryset
