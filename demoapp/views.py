from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Products, Category, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import uuid
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def global_user(request):
    profile = ''
    if request and request.user and request.user.id:
        profile = UserProfile.objects.filter(user_model=request.user).first()
    return profile

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
    context = {"categories": categories, "profile": global_user(request)} 
    return render(request, 'add_products.html', context=context)

def products(request):
    products = Products.objects.all()
    # select * from products
    print(products)

    context = {
        "products": products,
        "profile": global_user(request)
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
            product.image = image
            product.save()
        return redirect("products")
    context = {"product_details": product_details, "categories": categories, "message":message, "profile": global_user(request)}
    return render(request, 'update_products.html', context=context)

def delete_products(request, product_id):
    product = Products.objects.filter(id=product_id).first()
    if request.method == "POST":
        product.delete()
        return redirect("products")
        
    context = {"product": product, "profile": global_user(request)}
    return render(request, 'delete_products.html', context=context)

def user_registration(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        contact_detail = request.POST.get('contact_details')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        profile_image = request.FILES.get('profile_image')


        usern = User.objects.filter(username=username).first()
        usere = User.objects.filter(email=email).first()
        if usern:
            message = "Username already exists, please provide a different username"
        elif usere:
            message = "Email already exists, please provide a different email"
        elif password != confirmpassword:
            message = "Password and confirm password doesnot matches"
        else:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            profile = UserProfile(contact_detail=contact_detail, date_of_birth=date_of_birth, gender=gender, profile_image=profile_image, user_model=user)
            user.save()
            profile.save()
            return redirect("products")
    context = {'message': message, "profile": global_user(request)}
    return render(request, 'user_registration.html', context=context)

def user_login(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
        return redirect("products")
    context = {'message': message, "profile": global_user(request)}
    return render(request, 'login.html', context=context)

def user_logout(request):
    logout(request)
    return redirect('user_login') 

@csrf_exempt
def add_to_cart(request):
    try:
        if request.method == "POST":
            print("request received", request.POST.get('cart_value'))

        return JsonResponse({"data": "successfully added"}, safe=False)
    except Exception as e:
        return JsonResponse({"data": f"Something went wrong: {str(e)}"}, safe=False)
    
    
def order_placed(request):
    pass