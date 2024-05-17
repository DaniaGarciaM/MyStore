from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products

def index(request):
    #Listar todos los productos
    products = Products.objects.all()
    return render(request, 'list_of_products.html', {'products': products})
