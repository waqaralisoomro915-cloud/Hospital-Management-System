from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Billing
from .serializers import BillingSerializer

from ..accounts.models import User
from ..accounts.permissions import (
    IsAdmin,
    CanViewBilling
)


class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role in [
            User.Role.NURSE,
            User.Role.ADMIN,
        ]:
            return Billing.objects.all()

        elif user.role == User.Role.PATIENT:
            return Billing.objects.filter(
                patient__user=user
            )

        elif user.role == User.Role.DOCTOR:
            return Billing.objects.filter(
                patient__medical_records__doctor__user=user
            ).distinct()

        return Billing.objects.none()

    def get_permissions(self):

        if self.action == "destroy":
            permission_classes = [IsAdmin]

        elif self.action in [
            "create",
            "update",
            "partial_update"
        ]:
            permission_classes = [IsAdmin]

        elif self.action in [
            "list",
            "retrieve"
        ]:
            permission_classes = [CanViewBilling]

        else:
            permission_classes = [IsAuthenticated]

        return [
            permission()
            for permission in permission_classes
        ]