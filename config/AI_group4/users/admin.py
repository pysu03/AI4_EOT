from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'date_of_birth', 'gender', 'phone', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'date_of_birth', 'gender', 'phone',
                                      'address1', 'address2', 'address3')}),
        ('Important dates', {'fields': ('created_at', 'updated_at')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'date_of_birth', 'gender', 'phone',
                       'address1', 'address2', 'address3',
                       'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth import get_user_model
#
#
# class CustomUserAdmin(UserAdmin):
#     """Define admin model for custom User model with no username field."""
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name', 'date_of_birth')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                        'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'date_of_birth', 'password1', 'password2'),
#         }),
#     )
#     list_display = ('email', 'first_name', 'last_name', 'date_of_birth', 'is_staff')
#     search_fields = ('email', 'first_name', 'last_name')
#     ordering = ('email',)
#
#
# admin.site.register(get_user_model(), CustomUserAdmin)