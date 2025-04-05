from django.urls import path
from .views import admin_view, librarian_view, member_view, register
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    path('register/', register name='register'),
    path('logout/', LogoutView.as_view(template_name="logout_view")),
    path('login,', LoginView.as_view(template_name="login_view")),
]
