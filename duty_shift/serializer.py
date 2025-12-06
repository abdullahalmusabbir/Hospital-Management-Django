from rest_framework import serializers
from .models import DutyShift

class DutyShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = DutyShift
        fields = [
            'id',
            'name',
            'start_time',
            'end_time',
            'description',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class DutyShiftCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DutyShift
        fields = [
            'id',
            'name',
            'start_time',
            'end_time',
            'description',
        ]
