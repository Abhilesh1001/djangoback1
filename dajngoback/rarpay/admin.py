from django.contrib import admin
from .models import Tanctiction

# Register your models here.

@admin.register(Tanctiction)
class AdminTranction(admin.ModelAdmin):
    list_display = ['payment_id','order_id','signature','amount','datatime']
    