from django.contrib import admin
from .models import MedicineBill, MedicineBillItem


class MedicineBillItemInline(admin.TabularInline):
    model = MedicineBillItem
    extra = 1
    readonly_fields = ('total_price', 'created_at')


@admin.register(MedicineBill)
class MedicineBillAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_patient',
        'payment_status',
        'grand_total',
        'created_at',
    )
    list_filter = ('payment_status', 'created_at')
    search_fields = ('patient__user__username', 'medicine_items__medicine__name')
    readonly_fields = ('created_at', 'updated_at', 'grand_total')
    inlines = [MedicineBillItemInline]
    ordering = ('-created_at',)

    def get_patient(self, obj):
        return obj.patient.user.username
    get_patient.short_description = 'Patient'

    def grand_total(self, obj):
        return obj.calculate_grand_total()
    grand_total.short_description = 'Grand Total'
