from django.contrib import admin
from django.urls import path, include  # ✅ Import path and include
from django.shortcuts import redirect

def redirect_to_login(request):
    return redirect('login')  # Redirects to the login page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_login),  # Redirect root URL to login page
    path('relationship/', include('relationship_app.urls')),
]
