# ...existing code...
from django.shortcuts import render

def hello_world(request):
    return render(request, "hello.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
# ...existing code...