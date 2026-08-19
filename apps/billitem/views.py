from .models import BillItem
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..accounts.models import User
from ..accounts.permissions import (
    IsAdmin,
    CanViewBilling,
)

from .serializers import BillItemSerializer


class BillItemViewSet(viewsets.ModelViewSet):

    queryset = BillItem.objects.all()
    serializer_class = BillItemSerializer

    def get_queryset(self):
        user = self.request.user

        # Admin and Nurse can see all billing items
        if user.role in [
            User.Role.NURSE,
            User.Role.ADMIN,
        ]:
            return BillItem.objects.all()

        # Patient can see only their own billing items
        elif user.role == User.Role.PATIENT:
            return BillItem.objects.filter(
                billing__patient__user=user
            )

        # Doctor can see billing items of their patients
        elif user.role == User.Role.DOCTOR:
            return BillItem.objects.filter(
                billing__patient__doctor__user=user
            )

        return BillItem.objects.none()

    def get_permissions(self):

        # Only Admin can delete
        if self.action == "destroy":
            permission_classes = [IsAdmin]

        # Only Admin can create/update
        elif self.action in [
            "create",
            "update",
            "partial_update",
        ]:
            permission_classes = [IsAdmin]

        # Users allowed by CanViewBilling can list/retrieve
        elif self.action in [
            "list",
            "retrieve",
        ]:
            permission_classes = [CanViewBilling]

        # Other actions require authentication
        else:
            permission_classes = [IsAuthenticated]

        return [
            permission()
            for permission in permission_classes
        ]