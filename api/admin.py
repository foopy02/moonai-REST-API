from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from api.models import *

# Register your models here.

class MyUserAdmin(BaseUserAdmin):
    list_display=('email', 'username','date_joined','last_login', 'is_admin','is_active',)
    search_fields=('email','username')
    readonly_fields=('date_joined','last_login')
    filter_horizontal=()
    list_filter = ('username',)
    fieldsets=()

    # add_fieldsets=  (
    #     (None, {
    #         'classes':('wide'),
    #         'fields':('email','username','name','surname','gender','date_of_birth','password1','password2')
    #     }),
    # )

    ordering=('email',)
    
admin.site.register(CustomUser, MyUserAdmin)
admin.site.register(Withdraw)
admin.site.register(Deposit)