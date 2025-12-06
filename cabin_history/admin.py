from django.contrib import admin
from .models import CabinHistory, CabinMedicineUsage


class CabinMedicineUsageInline(admin.TabularInline):
    model = CabinMedicineUsage
    extra = 1
    readonly_fields = ('unit_price', 'total_price', 'created_at')


@admin.register(CabinHistory)
class CabinHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'patient',
        'cabin',
        'reference_doctor',
        'status',
        'payment_status',
        'total_cabin_charge',
        'total_medicine_cost',
        'grand_total',
        'admit_date',
        'discharge_date',
    )

    list_filter = (
        'status',
        'payment_status',
        'cabin__cabin_type',
        'cabin__floor',
        'reference_doctor',
        'admit_date',
    )

    search_fields = (
        'patient__user__username',
        'patient__user__first_name',
        'patient__user__last_name',
        'cabin__cabin_number',
    )

    readonly_fields = (
        'total_days',
        'total_medicine_cost',
        'total_doctor_fee',
        'total_cabin_charge',
        'grand_total',
        'created_at',
        'updated_at',
    )

    inlines = [CabinMedicineUsageInline]

    ordering = ('-created_at',)


@admin.register(CabinMedicineUsage)
class CabinMedicineUsageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cabin_history',
        'medicine',
        'quantity',
        'unit_price',
        'total_price',
        'created_at',
    )

    list_filter = ('medicine', 'created_at')
    search_fields = ('medicine__name', 'cabin_history__patient__user__username')
    readonly_fields = ('unit_price', 'total_price', 'created_at')
    ordering = ('-created_at',)
