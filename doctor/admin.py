from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'phone', 'experience_years', 'status', 'created_at')
    search_fields = ('user__username', 'specialization', 'phone', 'email')
    list_filter = ('specialization', 'gender', 'status', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'avatar', 'phone', 'email', 'address', 'gender', 'status')
        }),
        ('Professional Info', {
            'fields': ('specialization', 'qualification', 'experience_years', 'consultation_fee', 'available_from', 'available_to')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

admin.site.register(Doctor, DoctorAdmin)