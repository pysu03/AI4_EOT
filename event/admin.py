from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'start_time', 'created_date')
    list_filter = ('user',)
    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Event', {'fields': ('title', 'description', 'start_time')}),
        ('Important dates', {'fields': ('created_date',)}),
    )

    search_fields = ('user',)
    ordering = ('user',)
    filter_horizontal = ()


admin.site.register(Event, EventAdmin)


#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'name', 'date_of_birth', 'gender', 'phone',
#                        'address1', 'address2', 'address3',
#                        'password1', 'password2')}
#          ),
#     )
#
# admin.site.unregister(Group)