# from django.db import models
# from ..billing.models import Billing
#
#
# class BillItem(models.Model):
#
#     billing = models.ForeignKey(
#         Billing,
#         on_delete=models.CASCADE,
#         related_name="items"
#     )
#
#     item_type = models.CharField(
#         max_length=50
#     )
#
#     description = models.TextField(
#         blank=True,
#         null=True
#     )
#
#     amount = models.DecimalField(
#         max_digits=10,
#         decimal_places=2
#     )
#
#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )
#
#     def __str__(self):
#         return f"{self.item_type} - {self.amount}"