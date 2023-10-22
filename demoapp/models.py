from django.db import models
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User

#  Database manipulation with Meta Class
# https://docs.djangoproject.com/en/4.2/ref/models/options/
class Address(models.Model):
    line1 = models.CharField('line1', max_length=50)
    line2 = models.CharField('line2', max_length=50)
    zip_code = models.IntegerField()
    city = models.CharField('city', max_length=50)
    state = models.CharField('state', max_length=50)

    def __str__(self):
        return self.city
    
    class Meta:
        verbose_name_plural = "Address"


class Customers(models.Model):
    name = models.CharField('Name', max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    contact_detail = models.BigIntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Customers"


class Category(models.Model):
    name = models.CharField('name', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Category"


class Products(models.Model):
    name = models.CharField('name', max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    active = models.BooleanField(default=True)
    # category = models.CharField('category', max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    stock = models.IntegerField(default=1)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Products"


class UserProfile(models.Model):
    contact_detail = models.BigIntegerField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    profile_image = models.ImageField()
    user_model = models.ForeignKey(User, on_delete=models.CASCADE)

class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()

PAYMENT_TERMS = [
    ("COD", "COD"),
    ("Online", "Online"),
    ("EMI", "EMI"),
]

ORDER_STATUS = [
    ("Order Placed", "Order Placed"),
    ("Shipped", "Shipped"),
    ("Out for delivery", "Out for delivery"),
    ("Delivered", "Delivered"),
    ("Returned", "Returned"),
]
class Orders(models.Model):
    order_number = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    payment_terms = models.CharField(max_length = 20, choices = PAYMENT_TERMS)
    order_status = models.CharField(max_length = 20, choices = ORDER_STATUS, default="Order Placed")


# class MyUserManager(BaseUserManager):
#     def create_user(self, email, date_of_birth, password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not email:
#             raise ValueError("Users must have an email address")

#         user = self.model(
#             email=self.normalize_email(email),
#             date_of_birth=date_of_birth,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, date_of_birth, password=None):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#             date_of_birth=date_of_birth,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


# class MyUser(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name="email address",
#         max_length=255,
#         unique=True,
#     )
#     date_of_birth = models.DateField()
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = MyUserManager()

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["date_of_birth"]

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin