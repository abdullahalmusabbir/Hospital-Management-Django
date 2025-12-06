from django.contrib import admin
from .models import Pathologist

class PathologistAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'phone', 'experience_years', 'status', 'created_at')
    search_fields = ('user__username', 'department', 'phone', 'email')
    list_filter = ('department', 'gender', 'status', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'avatar', 'phone', 'email', 'address', 'gender', 'status')
        }),
        ('Professional Info', {
            'fields': ('department', 'qualification', 'experience_years')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

admin.site.register(Pathologist, PathologistAdmin)
