from django.db import models


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