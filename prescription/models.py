from django.db import models
from django.utils import timezone
from patient.models import Patient
from doctor.models import Doctor


class Prescription(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='prescriptions'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='prescriptions_given'
    )

    diagnosis = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    prescribed_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Prescription - {self.patient.user.username} - {self.prescribed_at.strftime('%Y-%m-%d %H:%M')}"


class PrescriptionMedicine(models.Model):
    """
    Stores medicines prescribed in each prescription
    """
    prescription = models.ForeignKey(
        Prescription,
        on_delete=models.CASCADE,
        related_name='medicines'
    )
    medicine_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100, blank=True, null=True)  # e.g., 1 tablet, 2 ml
    frequency = models.CharField(max_length=100, blank=True, null=True)  # e.g., twice a day
    duration = models.CharField(max_length=100, blank=True, null=True)  # e.g., 5 days
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.medicine_name} for {self.prescription.patient.user.username}"
