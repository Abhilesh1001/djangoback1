from django.contrib import admin
from .models import KartComment

# Register your models here.
@admin.register(KartComment)
class AdminKartComment(admin.ModelAdmin):
    list_display = ['sno','comment','user','product','parent','time']
