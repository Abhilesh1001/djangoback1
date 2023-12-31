from django.contrib import admin
from .models import NewContact,Product,Order,OrderUpdate,CartUserData
from django.contrib.sessions.models import Session

# Register your models here.

@admin.register(NewContact)
class AdminNewContact(admin.ModelAdmin):
    list_display = ['id','name','email','phone','desc']

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display=['product_id','product_name','category','desc','price','image','qty','uom']

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display=['order_id','items_json','name','email','date','address1','user','payment_id','amount','order_pay_id','signature']
    
@admin.register(OrderUpdate)
class AdminOrderUpdate(admin.ModelAdmin):
    list_display=['update_id','order_id','update_desc','timestamp']
    
@admin.register(CartUserData)
class AdminCartUserData(admin.ModelAdmin):
    list_display= ['cart_id','item_json','user']


@admin.register(Session)
class AdminSession(admin.ModelAdmin):
    list_display : ['session_key','session_data','session_date']