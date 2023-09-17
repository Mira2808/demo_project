from django.shortcuts import render
from django.http import HttpResponse
from .models import Products, Category

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is index</h1>")

def add_products(request):
    """
    function will create a new product from UI
    """
    if request.method == "POST":
        # print("inside post method")
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        stock = request.POST.get('stock')
        active = request.POST.get('active')

        category_name = Category.objects.filter(name=category).first()
        # SELECT * from category where name='Mobiles' limit 1;

        product_object = Products(name=product_name, 
                                  description=description, 
                                  price=price, category=category_name, stock=stock)
        product_object.save()
        print(product_object)
        
    return render(request, 'add_products.html')