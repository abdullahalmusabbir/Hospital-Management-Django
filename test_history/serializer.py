from rest_framework import serializers
from .models import TestHistory
from patient.serializers import PatientSerializer
from medical_test.serializer import MedicalTestSerializer


class TestHistorySerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    medical_test = MedicalTestSerializer(read_only=True)

    class Meta:
        model = TestHistory
        fields = [
            'id',
            'patient',
            'medical_test',
            'reference_doctor',
            'test_date',
            'status',
            'bill_paid_status',
            'report_delivery_status',
            'notes',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class TestHistoryCreateUpdateSerializer(serializers.ModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=PatientSerializer.Meta.model.objects.all(),
        source='patient',
        write_only=True
    )
    medical_test_id = serializers.PrimaryKeyRelatedField(
        queryset=MedicalTestSerializer.Meta.model.objects.all(),
        source='medical_test',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = TestHistory
        fields = [
            'id',
            'patient_id',
            'medical_test_id',
            'reference_doctor',
            'test_date',
            'status',
            'bill_paid_status',
            'report_delivery_status',
            'notes',
        ]

    def create(self, validated_data):
        return TestHistory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
