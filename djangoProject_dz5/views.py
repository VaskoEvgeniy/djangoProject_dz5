from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from djangoProject_dz5.models import Category
from product_page.models import Product
import random

def random_cost():
    cost = random.randint(10000, 20000)
    return cost

def homepage(request: HttpRequest)-> HttpResponse:

    custom_ctx_obj = {
        'category_list': Category.objects.all()

    }
    return render(request, 'Home_page.html', custom_ctx_obj)

def homepage_views(request: HttpRequest, username: str) -> HttpResponse:

    custom_ctx_obj = {
        'category_list': Category.objects.all()

    }
    return render(request, 'Home_page.html', custom_ctx_obj)

def product_category(request: HttpRequest, category_name: str) -> HttpResponse:
    try:
        ctx = {
            "product_list": Product.objects.filter(product_category__category_name=category_name)
        }
        return render(request, "Product_category.html", ctx)
    except :
        raise Http404('Not found')