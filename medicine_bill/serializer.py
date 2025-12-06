from rest_framework import serializers
from .models import MedicineBill, MedicineBillItem
from store_medicine.serializer import StoreMedicineSerializer


class MedicineBillItemSerializer(serializers.ModelSerializer):
    medicine_details = StoreMedicineSerializer(source='medicine', read_only=True)

    class Meta:
        model = MedicineBillItem
        fields = [
            'id',
            'medicine',
            'medicine_details',
            'quantity',
            'notes',
            'created_at',
            'total_price',
        ]
        read_only_fields = ['created_at', 'total_price']

    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        return obj.total_price()


class MedicineBillSerializer(serializers.ModelSerializer):
    medicine_items = MedicineBillItemSerializer(many=True, read_only=True)

    class Meta:
        model = MedicineBill
        fields = [
            'id',
            'patient',
            'payment_status',
            'notes',
            'created_at',
            'updated_at',
            'medicine_items',
        ]
        read_only_fields = ['created_at', 'updated_at']


class MedicineBillCreateUpdateSerializer(serializers.ModelSerializer):
    # Accept list of items for create/update
    medicine_items_data = MedicineBillItemSerializer(many=True, write_only=True)

    class Meta:
        model = MedicineBill
        fields = [
            'id',
            'patient',
            'payment_status',
            'notes',
            'medicine_items_data',
        ]

    def create(self, validated_data):
        items_data = validated_data.pop('medicine_items_data', [])
        bill = MedicineBill.objects.create(**validated_data)
        for item in items_data:
            MedicineBillItem.objects.create(bill=bill, **item)
        return bill

    def update(self, instance, validated_data):
        items_data = validated_data.pop('medicine_items_data', None)
        instance.payment_status = validated_data.get('payment_status', instance.payment_status)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()

        if items_data is not None:
            # Remove existing items and add new ones
            instance.medicine_items.all().delete()
            for item in items_data:
                MedicineBillItem.objects.create(bill=instance, **item)

        return instance
