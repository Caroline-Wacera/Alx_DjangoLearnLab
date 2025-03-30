# Retrieve the book from the database
book = Book.objects.get(title="1984")

# Display all attributes
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
