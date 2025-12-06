from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ITMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='it_member_profile', null=True, blank=True)
    
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    role = models.CharField(max_length=100, blank=True, null=True)  # Example: System Admin, Network Engineer, Support
    department = models.CharField(max_length=100, blank=True, null=True)  # e.g., IT, Networking
    qualification = models.CharField(max_length=100, blank=True, null=True)
    experience_years = models.PositiveIntegerField(blank=True, null=True)
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('on_leave', 'On Leave')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    
    avatar = models.ImageField(upload_to='it_member_avatars/', blank=True, null=True)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.role or 'No Role'}"
