from rest_framework import serializers
from .models import Appointment

from patient.models import Patient
from patient.serializer import PatientSerializer

from doctor.models import Doctor
from doctor.serializer import DoctorSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), source='patient', write_only=True
    )
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(), source='doctor', write_only=True
    )

    class Meta:
        model = Appointment
        fields = [
            'id',
            'patient',
            'doctor',
            'patient_id',
            'doctor_id',
            'appointment_date',
            'appointment_time',
            'status',
            'notes',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
