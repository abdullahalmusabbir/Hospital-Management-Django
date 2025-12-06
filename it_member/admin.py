from django.contrib import admin
from .models import ITMember

class ITMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'department', 'phone', 'experience_years', 'status', 'created_at')
    search_fields = ('user__username', 'role', 'department', 'phone', 'email')
    list_filter = ('role', 'department', 'gender', 'status', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'avatar', 'phone', 'email', 'address', 'gender', 'status')
        }),
        ('Professional Info', {
            'fields': ('role', 'department', 'qualification', 'experience_years')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

admin.site.register(ITMember, ITMemberAdmin)
