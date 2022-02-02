from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, redirect, render
from django.db import transaction
from django.contrib import messages
from .forms import ItemForm, UserForm
from django.contrib.auth.models import User
from .models import Product
# Create your views here.

def add_product(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        serial_number = form.cleaned_data["serial_number"]
        try:
            Product.objects.get(serial_number=serial_number)
            messages.error(request, "Item Already Exist")
        except Product.DoesNotExist:
            
            #user = User.objects.get(username=request.user)
            Product.objects.create(
                serial_number=serial_number,
                add_by="{}".format(str(request.user))
            )
            
            messages.success(request, "Added New item to inventory")
        return redirect('add_product')

    context = {
        "form": form
    }
    return render(request, 'add_product.html', context)


def login_(request):
    print (1)
    form = UserForm(request.POST or None)
    if form.is_valid():
        print (1)
        username = form.cleaned_data["username"]
        password = form.cleaned_data['password']
        
        try:
            user = User.objects.get(username=username)
            if user.is_active:
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('add_product')
                messages.error(request, 'Username/Password does not match')
            else:
                messages.error(
                    request, 'Authorisation Error Contact Admin To Regain Access')
        except Exception as e:
            messages.error(
                request, 'Username/Password does not match'.format())    
        
    context = {
        'form': form
    }
    return render(request, "login.html", context)


def add_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        try:
            user = User.objects.get(username=form.cleaned_data['username'])
            messages.error(request, "This user Aleady exist")
        except User.DoesNotExist:
            user = User()
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            user.username = username
            
            user.set_password(password)
            with transaction.atomic():
                user.save()
                messages.success(request, 'User Added')

    context = {
        "form": form,
        "users": User.objects.filter(is_staff=False)
    }
    return render(request, "new_user.html", context)


def search_product(request):
    form = ItemForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        serial_no = form.cleaned_data['serial_number']
        product = Product.objects.filter(serial_number=serial_no)
        context['products'] = product
        if not product.first():
            messages.error(request, "Item does not exist in our inventory")
    return render(request, "search_product.html", context)


def delete_user(request, id):
    user = get_object_or_404(User, id=id)

    user.delete()

    return redirect("add_user")