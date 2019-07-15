from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

''' _ ---> recommended notation for converting strings to text in Python'''
from django.utils.translation import gettext as _

from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        '''using gettext for the fieldset naming conventions'''
        (None, {'fields: ('email, 'password')}),
        (_('Personal Info'), {'fields': ('name',)}), #comma requried after 'name' so it's not considered a string
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )

admin.site.register(models.User, UserAdmin)
