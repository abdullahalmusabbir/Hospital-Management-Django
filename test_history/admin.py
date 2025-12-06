from django.contrib import admin
from .models import TestHistory


@admin.register(TestHistory)
class TestHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_patient',
        'get_test_name',
        'reference_doctor',
        'test_date',
        'status',
        'bill_paid_status',
        'report_delivery_status',
        'created_at',
    )
    list_filter = ('status', 'bill_paid_status', 'report_delivery_status', 'test_date', 'created_at')
    search_fields = (
        'patient__user__username',
        'medical_test__test_name',
        'reference_doctor'
    )
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-test_date',)

    def get_patient(self, obj):
        return obj.patient.user.username if obj.patient else "Unknown"
    get_patient.short_description = 'Patient'

    def get_test_name(self, obj):
        return obj.medical_test.test_name if obj.medical_test else "Unknown Test"
    get_test_name.short_description = 'Medical Test'
