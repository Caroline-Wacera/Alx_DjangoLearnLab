from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import BookForm  # Ensure you have a BookForm for adding/editing
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required

# permission_required decorator checks if the user has the required permission
# before allowing access to the view. If not, it raises a PermissionDenied exception.
# Where to use it:
# Use it on views where you want to restrict access based on permissions.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


@login_required
@permission_required('relationship_app.can_view_admin', raise_exception=True)
@user_passes_test(lambda u: u.userprofile.role == 'Admin', login_url='login')
def admin_view(request):
    if request.user.is_authenticated and request.user.userprofile.role == 'Admin':
        return render(request, 'relationship_app/admin_view.html')
    else:
        return redirect('login')
    
@login_required
@permission_required('relationship_app.can_view_librarian', raise_exception=True)
@user_passes_test(lambda u: u.userprofile.role == 'Librarian', login_url='login')
def librarian_view(request):
    if request.user.is_authenticated and request.user.userprofile.role == 'Librarian':
        return render(request, 'relationship_app/librarian_view.html')
    else:
        return redirect('login')
    
@login_required
@permission_required('relationship_app.can_view_member', raise_exception=True)
@user_passes_test(lambda u: u.userprofile.role == 'Member', login_url='login')
def member_view(request):
    if request.user.is_authenticated and request.user.userprofile.role == 'Member':
        return render(request, 'relationship_app/member_view.html')
    else:
        return redirect('login')


@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after adding
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})

@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})
