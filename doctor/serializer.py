from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Doctor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # User info read-only
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )  # Assign existing User when creating/updating doctor

    class Meta:
        model = Doctor
        fields = [
            'id',
            'user',
            'user_id',
            'phone',
            'address',
            'email',
            'specialization',
            'qualification',
            'experience_years',
            'consultation_fee',
            'available_from',
            'available_to',
            'gender',
            'status',
            'avatar',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
