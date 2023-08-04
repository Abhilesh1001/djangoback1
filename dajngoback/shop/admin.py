from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['msg_id','name','email','phone','desc']

