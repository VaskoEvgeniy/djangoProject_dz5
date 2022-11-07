from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from product_page.models import Product
# Create your views here.

def product_view(request: HttpRequest, category_name : str,product_name : str)-> HttpResponse:

    product = {
        'product': Product.objects.get(product_name=product_name),
        'category': category_name,
        'name_shop': product_name


    }
    return render(request, "Product_page.html", product)