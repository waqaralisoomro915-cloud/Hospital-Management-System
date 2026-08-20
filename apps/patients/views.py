from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..paginations import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from .models import Patient
from .serializers import PatientSerializer
from ..accounts.permissions import (
    CanViewPatient,
    IsAdmin,
    IsAdminOrDoctor,
)


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter,)
    filterset_fields = ("patient_id",)
    search_fields = ("patient_id",)
    ordering_fields = ("patient_id",)
    ordering = ("patient_id",)

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Patient.objects.none()


        if user.role in [
            user.Role.ADMIN,
            user.Role.DOCTOR,
            user.Role.NURSE,
        ]:
            return Patient.objects.all()

        if user.role == user.Role.PATIENT:
            return Patient.objects.filter(user=user)

        return Patient.objects.none()

    def get_permissions(self):

        if self.action == "destroy":
            permission_classes = [IsAdmin]

        elif self.action in ["create", "update", "partial_update"]:
            permission_classes = [IsAdminOrDoctor]

        elif self.action in ["list", "retrieve"]:
            permission_classes = [CanViewPatient]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]