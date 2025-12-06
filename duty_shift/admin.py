from django.contrib import admin
from .models import DutyShift


@admin.register(DutyShift)
class DutyShiftAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'start_time',
        'end_time',
        'description',
        'created_at',
    )
    list_filter = ('name', 'start_time', 'end_time', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('start_time',)
