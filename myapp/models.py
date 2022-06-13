from locale import format_string
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MainCategoryModel(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to ='MainCategory')
    info  = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class SubCategoryModel(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to ='subCategory')
    info  = models.CharField(max_length=200)


    def __str__(self):
        return self.name

st= (('New-Arrival','New-Arrival'),('Out-of-Stock','Out-of-Stock'))
class ProductModel(models.Model):
    mcate = models.ForeignKey(MainCategoryModel,on_delete=models.CASCADE)
    scate = models.ForeignKey(SubCategoryModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'Product')
    og_price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    discounted_price = models.IntegerField(default=0)
    sell_price = models.IntegerField(default=0)
    info = models.TextField()
    status = models.CharField(max_length=200,choices=st,default='New-Arrival')
    total_price = models.IntegerField(default=0)



    def __str__(self):
        return self.name

    def dis_price(self):
        return (self.og_price * self.discount)/100

    def s_price(self):
        return (self.og_price - self.dis_price())

    def save(self, *args, **kwargs):
        self.discounted_price = self.dis_price()
        self.sell_price = self.s_price()
        super(ProductModel, self).save(*args, **kwargs)

class CartModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def total_price(self):
        return(self.product.sell_price * self.quantity)


class AddressModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    phone = models.IntegerField()

    def __str__(self):
        return self.first_name

    def __str__(self):
        return self.address

status =(('ORDERPLACED','ORDERPLACED'),
('SHIPPED','SHIPPED'),
('ON THE WAY','ON THE WAY'),
('OUT FOR DELIVERY','OUT FOR DELIVERY'),
('CANCELLLED','CANCELLED')

)

class Placeorder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    address = models.ForeignKey(AddressModel,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20,choices=status,default="PENDING..")


    
  
  
