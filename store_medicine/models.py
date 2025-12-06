from django.db import models
from django.utils import timezone


class StoreMedicine(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100, blank=True, null=True)   # Tablet / Syrup / Injection

    generic_name = models.CharField(max_length=150, blank=True, null=True)
    manufacturer = models.CharField(max_length=150, blank=True, null=True)

    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)  # Total items in store
    min_stock_alert = models.PositiveIntegerField(default=5)  # Alert if less than this

    batch_number = models.CharField(max_length=100, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('out_of_stock', 'Out of Stock'),
        ('expired', 'Expired'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.generic_name or 'No Generic'})"

    def is_expired(self):
        """Check expiry status"""
        if self.expiry_date and self.expiry_date < timezone.now().date():
            return True
        return False

    def reduce_stock(self, qty):
        """Medicine usage system uses this."""
        if qty <= self.stock_quantity:
            self.stock_quantity -= qty
            self.save()
            return True
        return False
