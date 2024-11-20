import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, reverse
from main.forms import ProductForm
from main.models import Product

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.utils.html import strip_tags

import json
from django.http import JsonResponse

@login_required(login_url='/login')
def show_main(request):
    # product_list = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'npm': '2306213376', 
        'class_name': 'PBP B',  
        'app_name': 'Peonies Site',
        # 'product_list': product_list,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)  

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()  # Menyimpan data produk baru ke database
        return redirect('main:show_main')  
    
    context = {'form': form} 
    return render(request, "create_product.html", context) 

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      else:
            messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# Tugas baru
def edit_product(request, id):
    # Get product entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set product entry sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get product berdasarkan id
    product = Product.objects.get(pk = id)
    # Hapus product
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

# tugas 6
@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))   
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    bouquet_type = request.POST.get("bouquet_type")
    wrap_color = strip_tags(request.POST.get("wrap_color"))
    user = request.user

    new_product = Product(
        name=name,
        price=price,
        description=description,
        bouquet_type=bouquet_type,
        wrap_color=wrap_color,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = request.user if request.user.is_authenticated else None
            if user is None:
                return JsonResponse({"status": "error", "message": "User not authenticated"}, status=403)
            
            # Membuat produk baru
            new_product = Product.objects.create(
                user=user,
                name=data["name"],
                price=int(data["price"]),
                description=data["description"],
                bouquet_type=data["bouquet_type"],
                wrap_color=data["wrap_color"],
            )
            new_product.save()

            return JsonResponse({"status": "success"}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
    
@login_required
def get_user_product_json(request):
    product = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product))