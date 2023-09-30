from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hero, name="hero"),
    path('store/', views.store, name="store"),
    path('login/', views.LoginForm, name="login"),
    path('register/', views.RegisterForm, name="register"),
    path('logout/', views.LogoutForm, name="logout"),
    path('cart/', views.cart, name="cart"),
    path('description/<int:id>/', views.ProductDetail, name="description"), 
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]