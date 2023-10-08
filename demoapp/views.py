from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products, Category

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is index</h1>")

def add_products(request):
    """
    function will create a new product from UI
    """
    categories = Category.objects.all()
    if request.method == "POST":
        # print("inside post method")
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        stock = request.POST.get('stock')
        image = request.FILES.get("image")
        active = True if request.POST.get('active') == 'on' else False

        print(image)
        # Value if condition else value
        
        # if active == "on":
        #     active = True
        # else:
        #     active = False
        category_name = Category.objects.filter(name=category).first()
        # SELECT * from category where name='Mobiles' limit 1;

        product_object = Products(name=product_name, 
                                  description=description, 
                                  price=price, category=category_name,
                                  stock=stock, active=active,image=image)
        product_object.save()
        return redirect('products')     
    context = {"categories": categories} 
    return render(request, 'add_products.html', context=context)

def products(request):
    products = Products.objects.all()
    # select * from products
    print(products)


    context = {
        "products": products
    }
    return render(request, 'products.html', context=context)

def update_products(request, product_id):
    product_details = Products.objects.filter(id=product_id).first()
    # print("product_id", product_details)
    categories = Category.objects.all()
    message = ""
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        stock = request.POST.get('stock')
        image = request.FILES.get("image")
        active = True if request.POST.get('active') == 'on' else False

        if not product_name:
            message=  "product_name is mandatory"
        if not description:
            message= "description is mandatory"
        if not price:
            message= "price is mandatory"

        if not message:
            product = Products.objects.filter(id=product_id).first()
            category_name = Category.objects.filter(name=category).first()

            product.name = product_name
            product.description = description
            product.price = price
            product.category = category_name
            product.stock = stock
            product.active = active
            product.save()
        return redirect("products")
    context = {"product_details": product_details, "categories": categories, "message":message}
    return render(request, 'update_products.html', context=context)

def delete_products(request, product_id):
    product = Products.objects.filter(id=product_id).first()
    if request.method == "POST":
        product.delete()
        return redirect("products")
        
    context = {"product": product}
    return render(request, 'delete_products.html', context=context)