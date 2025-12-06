from django.contrib import admin
from .models import Cabin


@admin.register(Cabin)
class CabinAdmin(admin.ModelAdmin):
    list_display = (
        'cabin_number',
        'cabin_type',
        'floor',
        'building',
        'daily_rate',
        'is_available',
        'status',
    )

    list_filter = (
        'cabin_type',
        'floor',
        'building',
        'is_available',
        'status',
    )

    search_fields = (
        'cabin_number',
        'cabin_type',
        'building',
    )

    ordering = ('cabin_number',)
