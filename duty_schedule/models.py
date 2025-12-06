from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from duty_shift.models import DutyShift

User = get_user_model()


class DutySchedule(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='duty_schedules'
    )
    shift = models.ForeignKey(
        DutyShift,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='duty_schedules'
    )
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    STATUS_CHOICES = [
        ('assigned', 'Assigned'),
        ('completed', 'Completed'),
        ('absent', 'Absent'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='assigned')

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'shift', 'date')
        ordering = ['date', 'shift__start_time']

    def __str__(self):
        return f"{self.user.username} - {self.shift} - {self.date}"
