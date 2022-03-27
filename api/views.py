from django.shortcuts import render, redirect
from .models import Product, Shop, User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from .choices import USER_TYPE_CHOICES
from django.contrib import messages
from .forms import *
from datetime import datetime, timedelta
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, "api/home.html", context={})
    else:
        return redirect("/login")


def base(request):
    return render(request, "api/base.html", context={})

def cats(request):
    cats = Product.objects.all()
    return render(request,"api/cats.html",context={"cats":cats})

def sellers(request):
    return render(request,"api/sellers.html",context={})


# def signup(request):
#     if request.method == "POST":
#         fname = request.POST.get("fname")
#         lname = request.POST.get("lname")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         phone = request.POST.get("phone")
#         role = request.POST.get("role")
#         if role == "buyer":
#             role = 3
#         else:
#             role = 4
#         user = User.objects.create_user(
#             email=email,
#             password=password,
#             first_name=fname,
#             last_name=lname,
#             user_type=role,
#             phone=phone,
#         )
#         user.save()
#         return redirect("/login")
#     return render(request, "api/signup.html", context={})



def signup(request):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + username)
                return redirect('login')
            else:
                print(form.errors)            

        context = {'form':form}
        return render(request, 'api/signup.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


# def view_login(request):
#     if request.method == "POST":
#         print("login")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         # check if user has entered correct credentials
#         user = authenticate(email=email, password=password)
#         if user is not None:
#             login(request, user)
#             print("hogya")
#             # A backend authenticated the credentials
#             return redirect("/")
#         else:
#             return render(request, "api/login.html")
#         # No backend authenticated the credentials
#     return render(request, "api/login.html")

def view_login(request):
    if request.user.is_authenticated:
        print("Hi1")
        return redirect("/")
    else:
        if request.method == "POST":
            print("Hi2")
            username = request.POST.get("email")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Hi3")
                return redirect("/")
            else:
                messages.info(request, "Username OR password is incorrect")

        context = {}
        return render(request, "api/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect("/login")
