from django.db import models
from django.utils.timezone import now 
from customauth.models import User


# Create your models here.

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)

class NewContact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)


class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='shop/media')
    desc = models.CharField(max_length=300)
    pub_data = models.DateField()


class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000,default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=50,default='')
    email = models.EmailField(max_length=50,default='')
    address = models.EmailField(max_length=50,default='')
    address1 = models.CharField(max_length=50,default='')
    address2 = models.CharField(max_length=50,default='')
    city = models.CharField(max_length=50,default='')
    state = models.CharField(max_length=50,default='')
    zip = models.CharField(max_length=50,default='')
    date = models.DateTimeField(default=now)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add = True)


class CartUserData(models.Model):
    cart_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=5000)
    user = models.OneToOneField(User,on_delete=models.CASCADE)



class ExcelFile(models.Model):
    file = models.FileField(upload_to="excel")
