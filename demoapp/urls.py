from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add_products/', views.add_products, name="add_products"),
    path('products/', views.products, name="products"),
    path('update_products/<str:product_id>/', views.update_products, name="update_products"),
]