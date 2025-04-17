from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CustomUser




# admin.site.unregister(User)

# admin.site.register(CustomUser, UserAdmin)
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    readonly_fields = ("id",)
    for idx,fs in enumerate(UserAdmin.fieldsets):
        if fs[0] == 'Personal info':
            fs[-1]['fields'] = ('first_name', 'last_name', 'email', 'profile_picture')
            break
    
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.list_display = ("id",) + self.list_display

    
