from rest_framework import serializers
from .models import CabinBill
from cabin_history.serializer import CabinHistorySerializer
from prescription.serializer import PrescriptionSerializer


class CabinBillSerializer(serializers.ModelSerializer):
    cabin_history_details = CabinHistorySerializer(source='cabin_history', read_only=True)
    prescription_details = PrescriptionSerializer(source='prescription', read_only=True)

    class Meta:
        model = CabinBill
        fields = [
            'id',
            'cabin_history',
            'cabin_history_details',
            'prescription',
            'prescription_details',

            'total_days',
            'total_cabin_charge',
            'doctor_visit_fee',
            'medicine_charge',
            'grand_total',

            'payment_status',
            'notes',

            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'total_days',
            'total_cabin_charge',
            'doctor_visit_fee',
            'medicine_charge',
            'grand_total',
            'created_at',
            'updated_at',
        ]
