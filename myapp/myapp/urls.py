from django.contrib import admin
from django.urls import path, include
from .views import home  # Correct import from views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),  # Fixed the path and name
    path('emp/', include('emp.urls'))
]
