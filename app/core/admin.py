from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

''' _ ---> recommended notation for converting strings to text in Python'''
from django.utils.translation import gettext as _

from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        # using gettext for the fieldset naming conventions

        # top of the page, no title
        (None, {'fields': ('email', 'password')}),

        # User Personal Info section
        (_('Personal Info'), {'fields': ('name',)}), #comma requried after 'name' so it's not considered a string

        # User Permissions section
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser',)
            }
        ),

        # User Important Dates section
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    # used to customize the attributes for the user authentication
    # https://docs.djangoproject.com/en/2.2/topics/auth/customizing/
    add_fieldsets = (
        (None, {
            'classes': ('wide'), #default: allows input field to be full-screen
            'fields': ('email', 'password1', 'password2')
        }), #using a comma to ensure Python doesn't think this is an object
    )

admin.site.register(models.User, UserAdmin)
