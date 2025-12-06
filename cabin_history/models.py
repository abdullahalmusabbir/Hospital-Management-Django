from django.db import models
from django.utils import timezone
from patient.models import Patient
from doctor.models import Doctor
from cabin.models import Cabin
from store_medicine.models import StoreMedicine


class CabinHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='cabin_histories')
    cabin = models.ForeignKey(Cabin, on_delete=models.SET_NULL, null=True, related_name='cabin_histories')

    reference_doctor = models.ForeignKey(
        Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='referred_cabin_cases'
    )

    doctor_visit_count = models.PositiveIntegerField(default=0)
    doctor_visit_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Charges copied from Cabin
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    nursing_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    admit_date = models.DateTimeField(default=timezone.now)
    discharge_date = models.DateTimeField(blank=True, null=True)

    # Calculated fields
    total_days = models.PositiveIntegerField(default=1)
    total_medicine_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_doctor_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_cabin_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    PAYMENT_STATUS = [
        ('unpaid', 'Unpaid'),
        ('partial', 'Partial'),
        ('paid', 'Paid'),
    ]
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='unpaid')

    STATUS = [
        ('active', 'Active'),
        ('discharged', 'Discharged')
    ]
    status = models.CharField(max_length=15, choices=STATUS, default='active')

    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"CabinHistory - {self.patient.user.username}"


class CabinMedicineUsage(models.Model):
    """
    Stores medicine usage for each cabin history.
    """
    cabin_history = models.ForeignKey(
        CabinHistory,
        on_delete=models.CASCADE,
        related_name='medicine_usages'
    )
    medicine = models.ForeignKey(
        StoreMedicine,
        on_delete=models.SET_NULL,
        null=True,
        related_name='used_in_cabin'
    )
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self.medicine:
            self.unit_price = self.medicine.unit_price
            self.total_price = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.medicine} x {self.quantity} for {self.cabin_history}"
