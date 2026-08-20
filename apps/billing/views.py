from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from ..paginations import CustomPagination
from .models import Billing
from .serializers import BillingSerializer
from django_filters.rest_framework import DjangoFilterBackend
from ..accounts.models import User
from ..accounts.permissions import (
    IsAdmin,
    CanViewBilling
)


class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,OrderingFilter,SearchFilter,)
    filter_fields = ('status','patient__user')
    ordering_fields = ["bill_date","total_amount", "paid_amount","created_at", ]
    search_fields = [
 "patient__patient_id","patient__user__first_name","patient__user__last_name", ]
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
                patient__doctor__user=user)

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