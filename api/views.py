from re import U
from django.shortcuts import render, redirect
from .models import Product, Shop, User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from .choices import USER_TYPE_CHOICES
from django.contrib import messages
from .forms import *
from .filters import ShopFilter
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        return render(request, "api/home.html", context={})
    else:
        return redirect("login")

@login_required(login_url='login')
def buyer_dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        user = request.user
        subscriptions = Subscription.objects.filter(user=user.id)
        shops = Shop.objects.all()
        context = {"subscriptions": subscriptions, "user": user, "shops": shops}
        return render(request, "api/buyerDashboard.html", context)

@login_required(login_url='login')
def add_subscription(request):

    context = {}
    return render(request, "api/addSubscription.html", context)

@login_required(login_url='login')
def get_shop_products(request, pk):
    products = Product.objects.filter(shop=pk)
    context = {"products": products}
    return render(request, "api/allProducts.html", context)

@login_required(login_url='login')
def get_all_shops(request):
    shops = Shop.objects.all()
    filter = ShopFilter(request.GET, queryset=shops)
    shops = filter.qs
    context = {"shops": shops, "filter": filter}
    return render(request, "api/allShops.html", context)

@login_required(login_url='login')
def product_details(request, pk):
    form = CreateUserForm()
    product = Product.objects.get(id=pk)

    if request.method == "POST":
        weeks_list = [0 for i in range(7)]
        for key, value in request.POST.items():
            print(f"Key: {key}")
            print(f"Value: {value}")
            if "0" <= key <= "7":
                print("Hi")
                weeks_list[int(key)] = int(value)
        number_of_weeks = request.POST.get("week_counter")
        quantity = request.POST.get("counter")
        user = request.user
        shop = product.shop
        time_period = {"week_list": weeks_list}
        subscription = Subscription.objects.create(
            product=product,
            number_of_weeks=number_of_weeks,
            quantity=quantity,
            user=user,
            shop=shop,
            time_period=time_period,
        )
        subscription.save()
        return redirect("buyer_dashboard")

        # form = CreateUserForm(request.POST)
        # if form.is_valid():
        #     subscription = form.save()
        #     messages.success(request, 'Subscription Added')
        #     return redirect('buyer_dashboard')
        # else:
        #     print(form.errors)

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


@login_required(login_url='login')
def get_cart(request):
    user = request.user
    if not Cart.objects.filter(user=user.id).exists():
        cart = Cart.objects.create(user=user.id)
        cart.save()
    else:
        cart = Cart.objects.get(user=user.id)
    context = {
        'cart':cart
    }
    return render(request,"api/cart.html",cart)



