from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import *

# Create your views here.

def store(request):
    available_products = Product.get_all_available_products()
    context = {'available_products':available_products}
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
    form = LogInForm()
    if request.method == "POST":
        form = LogInForm(data=request.POST)
    context = {'form':form}
    return render(request, 'shop/login.html', context)

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        #if form.is_valid():
         #   form.save()
          #  return redirect('shop:store')
          
    # even though the form is not used for the form elements, it is used for the error messages
    context = {'form':form}
    return render(request, 'shop/signup.html', context)

def logout_user(request):
    logout(request)
    return redirect('shop:login')