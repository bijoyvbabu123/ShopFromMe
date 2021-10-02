from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate # login
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import *
from .forms import *

# Create your views here.

def store(request):
    available_products = Product.get_all_available_products()
    numberofcartitems = OrderItems.get_cart_items_number(request.user)
    
    # if the request is ajax.....
    if request.is_ajax :
        if request.method == "GET":
            if request.GET.get("action") == 'cartitems':
                customer = User.objects.get(username=request.GET.get("customer"))
                cartitems, netamount = OrderItems.get_cart_items(customer)
                # should make a dictionary {'id':quatity, 'id2': quantity,....} and pass the dictionary to JsonResponse
                items = {}
                for i in cartitems:
                    items[i.item.id] = i.quantity
                return JsonResponse(items)


    context = {
        'available_products':available_products,
        'numberofcartitems':numberofcartitems
    }
    return render(request, 'shop/store.html', context)

def cart(request):
    items, netamount = OrderItems.get_cart_items(request.user)
    numberofcartitems = OrderItems.get_cart_items_number(request.user)
    context = {
        'items':items,
        'numberofcartitems':numberofcartitems,
        'netamount':netamount
    }
    return render(request, 'shop/cart.html', context)

def checkout(request):
    items, netamount = OrderItems.get_cart_items(request.user)
    numberofcartitems = OrderItems.get_cart_items_number(request.user)
    context = {
        'items':items,
        'numberofcartitems':numberofcartitems,
        'netamount':netamount
    }
    return render(request, 'shop/checkout.html', context)

def order_history(request):
    numberofcartitems = OrderItems.get_cart_items_number(request.user)
    context = {
        'numberofcartitems':numberofcartitems
    }
    return render(request, 'shop/orderhistory.html', context)

def login(request):
    form = LogInForm()
    if request.method == "POST":
        form = LogInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)  # called like this, since the view name 'login' overrides auth.login
            return redirect('shop:store')
    context = {'form':form}
    return render(request, 'shop/login.html', context)

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, form.cleaned_data.get('username'))
            return redirect('shop:login')
          
    # even though the form is not used for the form elements, it is used for the error messages
    context = {'form':form}
    return render(request, 'shop/signup.html', context)

def logout_user(request):
    logout(request)
    return redirect('shop:login')