from django.contrib import admin
from .models import TestBill


class TestHistoryInline(admin.TabularInline):
    model = TestBill.test_histories.through
    extra = 1
    verbose_name = "Test History Entry"
    verbose_name_plural = "Test History Entries"


@admin.register(TestBill)
class TestBillAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_patient',
        'get_tests',
        'total_test_cost',
        'item_cost',
        'grand_total',
        'payment_status',
        'created_at',
    )
    list_filter = ('payment_status', 'created_at')
    search_fields = ('test_histories__medical_test__test_name', 'test_histories__patient__user__username')
    readonly_fields = ('total_test_cost', 'item_cost', 'grand_total', 'created_at', 'updated_at')
    inlines = [TestHistoryInline]
    ordering = ('-created_at',)

    def get_tests(self, obj):
        return ", ".join([
            th.medical_test.test_name if th.medical_test else "Unknown Test"
            for th in obj.test_histories.all()
        ])
    get_tests.short_description = 'Medical Tests'

    def get_patient(self, obj):
        first_history = obj.test_histories.first()
        if first_history:
            return first_history.patient.user.username
        return "Unknown"
    get_patient.short_description = 'Patient'
