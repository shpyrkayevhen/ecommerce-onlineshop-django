from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Account

# === MAKE THE CUSTOM PASSWORD FIELD READ ONLY === #
# class AccountAdmin(UserAdmin):
#     list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')    

#     filter_horizontal=()
#     list_filter = ()
#     fieldsets = ()

# admin.site.register(Account, AccountAdmin)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active']
    list_display_links = ['email', 'first_name', 'last_name']
    readonly_fields  = ['password', 'last_login', 'date_joined']
    ordering = ['-date_joined']