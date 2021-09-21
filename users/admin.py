from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from.models import User, Address


@admin.register(User)
class UserAdmin(UserAdmin):
    # add_form = ''
    # form = ''
    model = User
    list_display = ('email', 'first_name', 'last_name', 'cpf', 'address')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name', 'cpf')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('image',)}),
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'cpf', 'address')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('image',)}),
        (None, {'fields': ('email', 'password1', 'password2')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'cpf')})
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('zip_code', 'address', 'house_number', 'complement', 'neighborhood', 'city', 'state')
    list_filter = ('city', 'state')
    ordering = ('address',)
    search_fields = ('zip_code', 'address', 'neighborhood', 'city', 'state')
