from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # User info read-only
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )  # For assigning existing user when creating patient

    class Meta:
        model = Patient
        fields = [
            'id',
            'user',
            'user_id',
            'phone',
            'address',
            'age',
            'admitted',
            'gender',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
