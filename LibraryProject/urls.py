from django.contrib import admin
from django.urls import path, include
from relationship_app.views import home  # Import homepage view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Add this for the homepage
    path('relationship/', include('relationship_app.urls')),  # Include app URLs
]
