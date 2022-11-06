from django.urls import path
from product_page.views import product_view


urlpatterns = [
    path('ap-<slug:category_name>/ap-<str:product_name>', product_view, name='product')
]