from django.db import models
from ..departments.models import Department


class Room(models.Model):


    class RoomType(models.TextChoices):
        GENERAL = "GENERAL", "General"
        PRIVATE = "PRIVATE", "Private"
        ICU = "ICU", "ICU"
        SEMI_PRIVATE = "SEMI_PRIVATE", "Semi Private"

    class Status(models.TextChoices):
        AVAILABLE = "AVAILABLE", "Available"
        OCCUPIED = "OCCUPIED", "Occupied"
        MAINTENANCE = "MAINTENANCE", "Maintenance"

    room_number = models.CharField(max_length=20,unique=True)
    room_type = models.CharField(max_length=20,choices=RoomType.choices, default=RoomType.GENERAL)
    department = models.ForeignKey(Department,on_delete=models.PROTECT, related_name="rooms")
    status = models.CharField(max_length=20,choices=Status.choices,default=Status.AVAILABLE )
    capacity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True  )

    def __str__(self):
        return f"Room {self.room_number}"