from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect 
from main.forms import ProductForm
from main.models import Product

def show_main(request):
    product_list = Product.objects.all()
    context = {
        'name': 'Rizki Amani Hasanah',  
        'npm': '2306213376', 
        'class_name': 'PBP B',  
        'app_name': 'Peonies Site',
        'product_list': product_list
    }

    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)  

    if form.is_valid() and request.method == "POST":
        form.save()  # Menyimpan data produk baru ke database
        return redirect('main:show_main')  
    
    context = {'form': form} 
    return render(request, "create_product.html", context) 

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")