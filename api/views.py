from django.shortcuts import render, redirect
from .models import Product, Shop, User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from .choices import USER_TYPE_CHOICES
from django.contrib import messages
from .forms import *
from .filters import ShopFilter

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return render(request, "api/home.html", context={})
    else:
        return redirect("login")


def buyer_dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        user = request.user
        subscriptions = Subscription.objects.filter(user=user.id)
        shops = Shop.objects.all()
        context = {"subscriptions": subscriptions, "user": user, "shops": shops}
        return render(request, "api/buyerDashboard.html", context)


def add_subscription(request):

    context = {}
    return render(request, "api/addSubscription.html", context)


def get_shop_products(request, pk):
    products = Product.objects.filter(shop=pk)
    context = {"products": products}
    return render(request, "api/allProducts.html", context)


def get_all_shops(request):
    shops = Shop.objects.all()
    filter = ShopFilter(request.GET, queryset=shops)
    shops = filter.qs
    context = {"shops": shops, "filter": filter}
    return render(request, "api/allShops.html", context)


def product_details(request, pk):
    form = CreateUserForm()
    if request.method == "POST":
        for key, value in request.POST.items():
            print(f"Key: {key}")
            print(f"Value: {value}")
        number_of_weeks = request.POST.get("week_counter")
        quantity = request.POST.get("quantity")
        user = request.user

        # form = CreateUserForm(request.POST)
        # if form.is_valid():
        #     subscription = form.save()
        #     messages.success(request, 'Subscription Added')
        #     return redirect('buyer_dashboard')
        # else:
        #     print(form.errors)

    product = Product.objects.get(id=pk)
    context = {"product": product, "form": form}
    return render(request, "api/products.html", context)


def base(request):
    return render(request, "api/checkout.html", context={})


def sellers(request):
    return render(request, "api/sellers.html", context={})


def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + username)
            return redirect("login")
        else:
            print(form.errors)

    context = {"form": form}
    return render(request, "api/signup.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


def view_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST.get("email")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.info(request, "Username OR password is incorrect")

        context = {}
        return render(request, "api/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("/login")
