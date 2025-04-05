from django.urls import path
from .views import admin_view, librarian_view, member_view, register
import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    path('register/', views.register name='register'),
    path('logout/', LogoutView.as_view(template_name="logout_view")),
    path('login,', LoginView.as_view(template_name="login_view")),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]
