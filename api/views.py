from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "api/home.html", context={})

def base(request):
    return render(request, "api/base.html", context={})

def signup(request):
    return render(request, "api/signup.html", context={})

def login(request):
    return render(request, "api/login.html", context={})

