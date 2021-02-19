from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'time', 'address', 'description', 'completed')
    list_filter = ('user',)
    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Event', {'fields': ('title', 'description')}),
        ('Important dates', {'fields': ('created_date',)}),
    )

    search_fields = ('user',)
    ordering = ('user',)
    filter_horizontal = ()


admin.site.register(Event, EventAdmin)