from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def emp_home(request):
    return render(request, 'emp/home.html',{})

def add_emp(request):
    return render(request, 'emp/add_emp.html', {})