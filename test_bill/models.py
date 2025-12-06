from django.db import models
from django.utils import timezone
from test_history.models import TestHistory


class TestBill(models.Model):
    # Link to TestHistory entries instead of direct MedicalTest
    test_histories = models.ManyToManyField(
        TestHistory,
        related_name='test_bills',
        help_text='Select patient test history entries to include in this bill'
    )

    # Charges snapshot
    total_test_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    item_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)  # optional
    grand_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    PAYMENT_STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('partial', 'Partial'),
        ('paid', 'Paid'),
    ]
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='unpaid')

    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_totals(self):
        """Calculate total cost based on all linked test histories"""
        self.total_test_cost = sum(
            history.medical_test.cost if history.medical_test else 0
            for history in self.test_histories.all()
        )
        self.grand_total = self.total_test_cost + self.item_cost

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # save first to get M2M relationship
        self.calculate_totals()
        super().save(*args, **kwargs)

    def get_patient(self):
        first_history = self.test_histories.first()
        if first_history:
            return first_history.patient.user.username
        return "Unknown"

    def __str__(self):
        tests = ", ".join([
            h.medical_test.test_name if h.medical_test else "Unknown Test"
            for h in self.test_histories.all()
        ])
        return f"TestBill - {self.get_patient()} - {tests}"
