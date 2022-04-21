from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("base/", views.base, name="base"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.view_login, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("sellers/", views.sellers, name="sellers"),
    path("products/<str:pk>", views.product_details, name="product_details"),
    path(
        "edit-subscription/<str:pk>", views.edit_subscription, name="edit_subscription"
    ),
    path("shop-products/<str:pk>", views.get_shop_products, name="shop_products"),
    path("buyer-dashboard", views.buyer_dashboard, name="buyer_dashboard"),
    path("add-subscription", views.add_subscription, name="add_subscription"),
    path("shops/", views.get_all_shops, name="all_shops"),
    path("cart", views.get_cart, name="cart"),
    path("delete-from-cart/<str:pk>", views.delete_from_cart, name="delete_from_cart"),
    path("checkout", views.checkout, name="checkout"),
    path("placed", views.placed,name="placed"),
]
