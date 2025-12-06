from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'appointment_time', 'status', 'created_at')
    search_fields = ('patient__user__username', 'doctor__user__username', 'status', 'notes')
    list_filter = ('status', 'appointment_date', 'doctor__department')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('patient', 'doctor', 'appointment_date', 'appointment_time', 'status', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

admin.site.register(Appointment, AppointmentAdmin)
