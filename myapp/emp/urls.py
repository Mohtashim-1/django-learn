from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home/', emp_home),
    # path('add-emp', add_emp),
     path('add-emp/', add_emp, name='add-emp'),  # Named URL pattern for add-emp
]