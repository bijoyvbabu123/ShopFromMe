from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def store(request):
    context = {'products': range(15)}
    return render(request, 'shop/store.html', context)

def cart(request):
    context = {}
    return render(request, 'shop/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html', context)

def order_history(request):
    context = {}
    return render(request, 'shop/orderhistory.html', context)

def login(request):
    context = {}
    return render(request, 'shop/login.html', context)

def signup(request):
    context = {}
    return render(request, 'shop/signup.html', context)

def logout_user(request):
    logout(request)
    return redirect('shop:login')