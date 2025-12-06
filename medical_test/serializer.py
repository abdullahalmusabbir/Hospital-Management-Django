from rest_framework import serializers
from .models import *


class MedicalTestItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalTestItem
        fields = [
            'id',
            'item_name',
            'quantity',
            'notes',
            'created_at',
        ]
        read_only_fields = ['created_at']


class MedicalTestSerializer(serializers.ModelSerializer):
    items = MedicalTestItemSerializer(many=True, read_only=True)

    class Meta:
        model = MedicalTest
        fields = [
            'id',
            'patient',
            'reference_doctor',  # doctor name string
            'test_name',
            'description',
            'cost',
            'status',
            'scheduled_date',
            'performed_date',
            'report_ready',
            'created_at',
            'updated_at',
            'items',  # related items
        ]
        read_only_fields = ['created_at', 'updated_at']
