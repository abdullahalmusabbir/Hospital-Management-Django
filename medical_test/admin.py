from django.contrib import admin
from .models import *


class MedicalTestItemInline(admin.TabularInline):
    model = MedicalTestItem
    extra = 1
    readonly_fields = ('created_at',)


@admin.register(MedicalTest)
class MedicalTestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'test_name',
        'patient',
        'reference_doctor',
        'status',
        'scheduled_date',
        'performed_date',
        'report_ready',
    )
    list_filter = ('status', 'report_ready', 'scheduled_date')
    search_fields = ('test_name', 'patient__user__username', 'reference_doctor')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [MedicalTestItemInline]
    ordering = ('-scheduled_date',)


@admin.register(MedicalTestItem)
class MedicalTestItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'medical_test',
        'item_name',
        'quantity',
        'created_at',
    )
    list_filter = ('item_name',)
    search_fields = ('item_name', 'medical_test__patient__user__username')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
