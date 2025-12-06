from django.db import models
from django.utils import timezone
from patient.models import Patient
from store_medicine.models import StoreMedicine


class MedicineBill(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='medicine_bills'
    )

    PAYMENT_STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('partial', 'Partial'),
        ('paid', 'Paid'),
    ]
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='unpaid')
    notes = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_grand_total(self):
        return sum(item.total_price() for item in self.medicine_items.all())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Optional: update grand_total if you have a field to store it

    def __str__(self):
        return f"MedicineBill - {self.patient.user.username} - {self.id}"


class MedicineBillItem(models.Model):
    bill = models.ForeignKey(
        MedicineBill,
        on_delete=models.CASCADE,
        related_name='medicine_items'
    )
    medicine = models.ForeignKey(
        StoreMedicine,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    quantity = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)

    def total_price(self):
        if self.medicine:
            return self.medicine.price * self.quantity
        return 0

    def __str__(self):
        med_name = self.medicine.name if self.medicine else "Unknown"
        return f"{med_name} x{self.quantity} for {self.bill.patient.user.username}"
