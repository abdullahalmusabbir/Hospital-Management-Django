from django.db import models
from django.utils import timezone
from patient.models import Patient
from doctor.models import Doctor


class MedicalTest(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='medical_tests'
    )

    reference_doctor = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        help_text="Select from existing doctors or enter name manually"
    )

    TEST_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    test_name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=TEST_STATUS_CHOICES, default='pending')

    scheduled_date = models.DateTimeField(blank=True, null=True)
    performed_date = models.DateTimeField(blank=True, null=True)
    report_ready = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.test_name} - {self.patient.user.username} - {self.reference_doctor or 'Unknown'}"

class MedicalTestItem(models.Model):
    """
    Extra items required for the test, e.g., tubes, reagents, containers
    """
    medical_test = models.ForeignKey(
        MedicalTest,
        on_delete=models.CASCADE,
        related_name='items'
    )
    item_name = models.CharField(max_length=150)  # e.g., EDTA Tube, Serum Tube
    quantity = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.item_name} x{self.quantity} for {self.medical_test.test_name}"