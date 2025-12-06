from django.db import models
from django.utils import timezone
from patient.models import Patient
from medical_test.models import MedicalTest


class TestHistory(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='test_history'
    )

    medical_test = models.ForeignKey(
        MedicalTest,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='history'
    )

    reference_doctor = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        help_text='Doctor who recommended the test'
    )

    test_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('reviewed', 'Reviewed'),
        ],
        default='pending'
    )

    # New fields
    BILL_STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('partial', 'Partial'),
        ('paid', 'Paid'),
    ]
    bill_paid_status = models.CharField(
        max_length=10,
        choices=BILL_STATUS_CHOICES,
        default='unpaid',
        help_text='Payment status from TestBill'
    )

    REPORT_DELIVERY_CHOICES = [
        ('pending', 'Pending'),
        ('delivered', 'Delivered'),
        ('none', 'None'),
    ]
    report_delivery_status = models.CharField(
        max_length=10,
        choices=REPORT_DELIVERY_CHOICES,
        default='none',
        help_text='Delivery status of the test report'
    )

    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        test_name = self.medical_test.test_name if self.medical_test else "Unknown Test"
        return f"{test_name} - {self.patient.user.username} - {self.status}"
