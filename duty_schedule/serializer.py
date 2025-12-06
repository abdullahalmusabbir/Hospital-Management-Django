from rest_framework import serializers
from .models import DutySchedule
from duty_shift.serializer import DutyShiftSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class DutyScheduleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    shift = DutyShiftSerializer(read_only=True)

    class Meta:
        model = DutySchedule
        fields = [
            'id',
            'user',
            'shift',
            'date',
            'status',
            'notes',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class DutyScheduleCreateUpdateSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user',
        write_only=True
    )
    shift_id = serializers.PrimaryKeyRelatedField(
        queryset=DutyShiftSerializer.Meta.model.objects.all(),
        source='shift',
        write_only=True,
        allow_null=True,
        required=False
    )

    class Meta:
        model = DutySchedule
        fields = [
            'id',
            'user_id',
            'shift_id',
            'date',
            'status',
            'notes',
        ]

    def create(self, validated_data):
        return DutySchedule.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
