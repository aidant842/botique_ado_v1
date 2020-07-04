from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    # specify that product id must be an int, otherwise
    # navigating to products/add will interperate the
    # string as an id and throw an error
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]
