from django.contrib import admin
from .models import Cashier

class CashierAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'role', 'phone', 'experience_years', 'status', 'created_at')
    search_fields = ('user__username', 'department', 'role', 'phone', 'email')
    list_filter = ('department', 'role', 'gender', 'status', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'avatar', 'phone', 'email', 'address', 'gender', 'status')
        }),
        ('Professional Info', {
            'fields': ('department', 'role', 'experience_years')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

admin.site.register(Cashier, CashierAdmin)
