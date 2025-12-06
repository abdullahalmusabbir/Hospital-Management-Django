from rest_framework import serializers
from .models import *
from patient.serializer import PatientSerializer
from doctor.serializer import DoctorSerializer


class PrescriptionMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionMedicine
        fields = [
            'id',
            'medicine_name',
            'dosage',
            'frequency',
            'duration',
            'notes',
            'created_at',
        ]
        read_only_fields = ['created_at']


class PrescriptionSerializer(serializers.ModelSerializer):
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)
    medicines = PrescriptionMedicineSerializer(many=True, read_only=True)

    class Meta:
        model = Prescription
        fields = [
            'id',
            'patient',
            'patient_details',
            'doctor',
            'doctor_details',
            'diagnosis',
            'notes',
            'prescribed_at',
            'updated_at',
            'medicines',
        ]
        read_only_fields = ['prescribed_at', 'updated_at']
