from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def onetimeride(request):
    return render(request, 'onetimeride.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')