from rest_framework import serializers
from .models import TestBill
from test_history.models import TestHistory
from test_history.serializers import TestHistorySerializer


class TestBillSerializer(serializers.ModelSerializer):
    test_histories = TestHistorySerializer(many=True, read_only=True)

    class Meta:
        model = TestBill
        fields = [
            'id',
            'test_histories',
            'total_test_cost',
            'item_cost',
            'grand_total',
            'payment_status',
            'notes',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'total_test_cost',
            'item_cost',
            'grand_total',
            'created_at',
            'updated_at',
        ]


class TestBillCreateUpdateSerializer(serializers.ModelSerializer):
    # Accept list of TestHistory IDs for creation/updation
    test_histories_ids = serializers.PrimaryKeyRelatedField(
        queryset=TestHistory.objects.all(),
        many=True,
        write_only=True
    )

    class Meta:
        model = TestBill
        fields = [
            'id',
            'test_histories_ids',
            'payment_status',
            'notes',
        ]

    def create(self, validated_data):
        test_histories = validated_data.pop('test_histories_ids', [])
        bill = TestBill.objects.create(**validated_data)
        bill.test_histories.set(test_histories)
        bill.calculate_totals()
        bill.save()
        return bill

    def update(self, instance, validated_data):
        test_histories = validated_data.pop('test_histories_ids', None)
        if test_histories is not None:
            instance.test_histories.set(test_histories)
        instance.payment_status = validated_data.get('payment_status', instance.payment_status)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.calculate_totals()
        instance.save()
        return instance
