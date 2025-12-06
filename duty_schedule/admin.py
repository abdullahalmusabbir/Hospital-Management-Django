from django.contrib import admin
from .models import DutySchedule


@admin.register(DutySchedule)
class DutyScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_user',
        'get_shift',
        'date',
        'status',
        'notes',
        'created_at',
    )
    list_filter = ('status', 'date', 'shift')
    search_fields = ('user__username', 'shift__name', 'notes')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-date', 'shift__start_time')

    def get_user(self, obj):
        return obj.user.username if obj.user else "Unknown"
    get_user.short_description = 'User'

    def get_shift(self, obj):
        return str(obj.shift) if obj.shift else "No Shift"
    get_shift.short_description = 'Shift'
