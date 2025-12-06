from rest_framework import serializers
from .models import CabinHistory, CabinMedicineUsage
from patient.serializers import PatientSerializer
from doctor.serializers import DoctorSerializer
from cabin.serializers import CabinSerializer
from store_medicine.serializers import StoreMedicineSerializer


class CabinMedicineUsageSerializer(serializers.ModelSerializer):
    medicine_details = StoreMedicineSerializer(source='medicine', read_only=True)

    class Meta:
        model = CabinMedicineUsage
        fields = [
            'id',
            'medicine',
            'medicine_details',
            'quantity',
            'unit_price',
            'total_price',
            'created_at'
        ]
        read_only_fields = ['unit_price', 'total_price']


class CabinHistorySerializer(serializers.ModelSerializer):
    patient_details = PatientSerializer(source='patient', read_only=True)
    cabin_details = CabinSerializer(source='cabin', read_only=True)
    reference_doctor_details = DoctorSerializer(source='reference_doctor', read_only=True)

    medicine_usages = CabinMedicineUsageSerializer(many=True, read_only=True)

    class Meta:
        model = CabinHistory
        fields = [
            'id',
            'patient',
            'patient_details',
            'cabin',
            'cabin_details',
            'reference_doctor',
            'reference_doctor_details',

            'doctor_visit_count',
            'doctor_visit_fee',

            'daily_rate',
            'service_charge',
            'nursing_charge',

            'admit_date',
            'discharge_date',

            'total_days',
            'total_medicine_cost',
            'total_doctor_fee',
            'total_cabin_charge',
            'grand_total',

            'payment_status',
            'status',
            'notes',

            'medicine_usages',

            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'total_medicine_cost',
            'total_doctor_fee',
            'total_cabin_charge',
            'grand_total'
        ]
