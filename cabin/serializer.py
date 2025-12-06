from rest_framework import serializers
from .models import Cabin


class CabinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabin
        fields = [
            'id',
            'cabin_number',
            'cabin_type',
            'floor',
            'building',

            'daily_rate',
            'is_available',

            'has_ac',
            'has_tv',
            'has_attached_bath',
            'bed_count',

            'nursing_charge',
            'service_charge',

            'description',
            'status',

            'created_at',
            'updated_at',
        ]
