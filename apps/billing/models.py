from django.db import models
from ..patients.models import Patient


class Billing(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "PENDING"),
        ("PARTIAL", "PARTIAL"),
        ("PAID", "PAID"),
        ("CANCELLED", "CANCELLED"),
    ]

    patient = models.ForeignKey(
        Patient,
        on_delete=models.PROTECT,
        related_name="bills"
    )

    bill_date = models.DateField(auto_now_add=True)

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    paid_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient} - {self.total_amount}"

