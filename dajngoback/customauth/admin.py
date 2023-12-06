from django.contrib import admin
from .models import User,ProfileUpdate
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ["id","email", "name","tc", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name","tc"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "tc","password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email",'id']
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)

@admin.register(ProfileUpdate)
class AdminProfileUpdata(admin.ModelAdmin):
    list_display = ['user','Date_of_Birth','profile_picture']
