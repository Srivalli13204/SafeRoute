from django.db import models

from django.contrib.auth.models import User

class EmergencyFacility(models.Model):
    FACILITY_TYPES = [
        ("medical", "Medical"),
        ("fire", "Fire"),
        ("police", "Police"),
    ]

    name = models.CharField(max_length=200)
    facility_type = models.CharField(
        max_length=20,
        choices=FACILITY_TYPES
    )
    address = models.TextField()
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )
    longitude = models.DecimalField(
            max_digits=9,
            decimal_places=6
    )
    contact = models.CharField(max_length=15)
    emergency_service = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class EmergencyRequest(models.Model):

    EMERGENCY_TYPES = [
        ("medical", "Medical"),
        ("accident", "Accident"),
        ("fire", "Fire"),
        ("police", "Police"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    emergency_type = models.CharField(
        max_length=20,
        choices=EMERGENCY_TYPES
    )

    source_location = models.CharField(
        max_length=255
    )

    destination = models.CharField(
        max_length=255
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    def __str__(self):
        return f"{self.emergency_type} - {self.source_location}"