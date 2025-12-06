from django.contrib import admin
from .models import Prescription, PrescriptionMedicine


class PrescriptionMedicineInline(admin.TabularInline):
    model = PrescriptionMedicine
    extra = 1
    readonly_fields = ('created_at',)


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'patient',
        'doctor',
        'prescribed_at',
        'updated_at',
    )

    list_filter = (
        'doctor',
        'prescribed_at',
    )

    search_fields = (
        'patient__user__username',
        'doctor__user__username',
        'diagnosis',
    )

    readonly_fields = ('prescribed_at', 'updated_at')

    inlines = [PrescriptionMedicineInline]

    ordering = ('-prescribed_at',)


@admin.register(PrescriptionMedicine)
class PrescriptionMedicineAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'prescription',
        'medicine_name',
        'dosage',
        'frequency',
        'duration',
        'created_at',
    )

    list_filter = ('medicine_name', 'created_at')
    search_fields = ('medicine_name', 'prescription__patient__user__username')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
