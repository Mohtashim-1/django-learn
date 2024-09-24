from django.shortcuts import render

def home(request):
    return render(request, 'navbar.html')  # Ensure this path is correct
