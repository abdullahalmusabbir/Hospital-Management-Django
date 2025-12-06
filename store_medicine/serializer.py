from rest_framework import serializers
from .models import StoreMedicine


class StoreMedicineSerializer(serializers.ModelSerializer):
    is_expired = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = StoreMedicine
        fields = [
            'id',
            'name',
            'generic_name',
            'category',
            'manufacturer',
            'unit_price',
            'stock_quantity',
            'min_stock_alert',
            'batch_number',
            'expiry_date',
            'status',
            'description',
            'is_expired',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['is_expired', 'created_at', 'updated_at']

    def get_is_expired(self, obj):
        return obj.is_expired()
