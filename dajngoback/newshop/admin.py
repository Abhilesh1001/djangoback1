from django.contrib import admin
from .models import NewContact,Product,Order,OrderUpdate,CartUserData

# Register your models here.

@admin.register(NewContact)
class AdminNewContact(admin.ModelAdmin):
    list_display = ['id','name','email','phone','desc']

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display=['product_id','product_name','category','desc','price','image']

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display=['order_id','items_json','name','email','date','address1','user']
    
@admin.register(OrderUpdate)
class AdminOrderUpdate(admin.ModelAdmin):
    list_display=['update_id','order_id','update_desc','timestamp']
    
@admin.register(CartUserData)
class AdminCartUserData(admin.ModelAdmin):
    list_display= ['cart_id','item_json','user']

