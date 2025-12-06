from django.contrib import admin
from .models import StoreMedicine


@admin.register(StoreMedicine)
class StoreMedicineAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'generic_name',
        'category',
        'manufacturer',
        'unit_price',
        'stock_quantity',
        'status',
        'expiry_date',
        'min_stock_alert',
    )

    list_filter = (
        'category',
        'manufacturer',
        'status',
        'expiry_date',
    )

    search_fields = (
        'name',
        'generic_name',
        'manufacturer',
        'batch_number',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    ordering = ('name',)
