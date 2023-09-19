from django.db import models
from customauth.models import User
from newshop.models import Product
from django.utils.timezone import now 

# Create your models here.

class KartComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    time = models.DateTimeField(default=now)


