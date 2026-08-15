from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Patient
from .serializers import PatientSerializer
from ..accounts.permissions import (
    CanViewPatient,
    IsAdmin,
    IsAdminOrDoctor,
)


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer

    def get_queryset(self):
        user = self.request.user

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