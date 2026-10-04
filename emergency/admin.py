from django.contrib import admin
from .models import EmergencyFacility, EmergencyRequest

# Register your models here.
@admin.register(EmergencyFacility)
class EmergencyFacilityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "facility_type",
        "address",
        "emergency_service",
        "is_active",
    )

    list_filter = (
        "facility_type",
        "emergency_service",
        "is_active",
    )

    search_fields = (
        "name",
        "address",
    )

@admin.register(EmergencyRequest)
class EmergencyRequestAdmin(admin.ModelAdmin):
    list_display = (
        "emergency_type",
        "source_location",
        "destination",
        "status",
        "created_at",
    )

    list_filter = (
        "emergency_type",
        "status",
    )

    search_fields = (
        "source_location",
        "destination",
    )