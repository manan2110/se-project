from email.mime import base
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("base/", views.base, name="base"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.view_login, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("cats/", views.cats, name="cats"),
    path("sellers/", views.sellers, name="sellers"),
     path("products/<str:pk>", views.products,name="products"),
]
