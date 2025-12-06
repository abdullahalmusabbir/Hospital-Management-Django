from django.db import models
from django.utils import timezone

class DutyShift(models.Model):
    SHIFT_CHOICES = [
        ('morning', 'Morning'),
        ('evening', 'Evening'),
        ('night', 'Night'),
    ]

    name = models.CharField(max_length=50, choices=SHIFT_CHOICES, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['start_time']
        verbose_name = 'Duty Shift'
        verbose_name_plural = 'Duty Shifts'

    def __str__(self):
        return f"{self.get_name_display()} ({self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')})"
