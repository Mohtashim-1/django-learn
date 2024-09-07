from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world! you are in home page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse('Hello, world! you are in about page')

def contact(request):
    return HttpResponse('hello, world! you are in contact page')