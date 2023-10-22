from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add_products/', views.add_products, name="add_products"),
    path('products/', views.products, name="products"),
    path('update_products/<str:product_id>/', views.update_products, name="update_products"),
    path('delete_products/<str:product_id>/', views.delete_products, name="delete_products"),
    path('user_registration/', views.user_registration, name='user_registration'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('order_placed/', views.order_placed, name='order_placed'),
]