from django.shortcuts import render, redirect

# Create your views here.

def store(request):
    context = {}
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

def logout(request):
    logout(request)
    return redirect('shop:login')