from django.db import models
from django.utils import timezone


class Cabin(models.Model):

    # Basic info
    cabin_number = models.CharField(max_length=20, unique=True)
    cabin_type = models.CharField(max_length=100)    # General, Deluxe, VIP, ICU, CCU
    floor = models.CharField(max_length=20, blank=True, null=True)
    building = models.CharField(max_length=50, blank=True, null=True)

    # Pricing & availability
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    # Specifications
    has_ac = models.BooleanField(default=False)
    has_tv = models.BooleanField(default=False)
    has_attached_bath = models.BooleanField(default=True)
    bed_count = models.PositiveIntegerField(default=1)

    # Optional extra charges
    nursing_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Description
    description = models.TextField(blank=True, null=True)

    # Tracking
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('cleaning', 'Cleaning'),
        ('maintenance', 'Maintenance'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"Cabin {self.cabin_number} ({self.cabin_type})"
