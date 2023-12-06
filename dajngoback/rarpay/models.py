from django.db import models
from customauth.models import User

# Create your models here.

class Tanctiction(models.Model):
    payment_id = models.CharField(max_length=100,verbose_name="Payment Id")
    order_id = models.CharField(max_length=100,verbose_name="Order Id")
    signature = models.CharField(max_length=200,verbose_name="Signature")
    amount = models.IntegerField(verbose_name="Amount")
    datatime=models.DateField(auto_now_add=True)


