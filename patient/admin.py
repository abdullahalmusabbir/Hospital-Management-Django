from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'age', 'admitted', 'gender', 'created_at')
    search_fields = ('user__username', 'phone', 'address')
    list_filter = ('gender', 'created_at')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Patient, PatientAdmin)
