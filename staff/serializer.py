from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Staff

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # User info nested format e show korbe
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )  # Staff create/update er somoy existing User assign kora jabe

    class Meta:
        model = Staff
        fields = [
            'id',
            'user',
            'user_id',
            'phone',
            'address',
            'email',
            'department',
            'role',
            'experience_years',
            'gender',
            'status',
            'avatar',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
