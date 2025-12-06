from django.db import models
from django.utils import timezone
from cabin_history.models import CabinHistory
from prescription.models import Prescription  # Prescription model from prescription app


class CabinBill(models.Model):
    cabin_history = models.OneToOneField(
        CabinHistory,
        on_delete=models.CASCADE,
        related_name='cabin_bill'
    )

    # Discharge prescription
    prescription = models.OneToOneField(
        Prescription,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cabin_bill'
    )

    # Charges copied from cabin_history
    total_days = models.PositiveIntegerField(default=1)
    total_cabin_charge = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    doctor_visit_fee = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    medicine_charge = models.DecimalField(max_digits=12, decimal_places=2, default=0)
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
        """Copy charges from cabin_history and calculate grand total"""
        ch = self.cabin_history
        if ch.discharge_date:
            self.total_days = (ch.discharge_date.date() - ch.admit_date.date()).days + 1
        else:
            self.total_days = 1

        self.total_cabin_charge = (ch.daily_rate * self.total_days) + ch.service_charge + ch.nursing_charge
        self.doctor_visit_fee = ch.total_doctor_fee
        self.medicine_charge = ch.total_medicine_cost
        self.grand_total = self.total_cabin_charge + self.doctor_visit_fee + self.medicine_charge

    def save(self, *args, **kwargs):
        self.calculate_totals()
        super().save(*args, **kwargs)

    def __str__(self):
        patient_name = self.cabin_history.patient.user.username if self.cabin_history.patient else "Unknown"
        cabin_number = self.cabin_history.cabin.cabin_number if self.cabin_history.cabin else "N/A"
        return f"CabinBill - {patient_name} - {cabin_number}"
