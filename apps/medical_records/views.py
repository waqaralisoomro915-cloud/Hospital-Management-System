from rest_framework import viewsets

from .models import MedicalRecord
from .serializers import MedicalRecordSerializer
from ..accounts.models import User
from ..accounts.permissions import (IsAdmin,IsAdminOrDoctor,CanViewMedical_record)
from rest_framework.permissions import IsAuthenticated


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role in [
            User.Role.NURSE,
            User.Role.ADMIN,
        ]:
            return MedicalRecord.objects.all()
        elif user.role == User.Role.PATIENT:
            return MedicalRecord.objects.filter(patient__user=user)
        elif user.role == User.Role.DOCTOR:
            return MedicalRecord.objects.filter(doctor__user=user)

        return MedicalRecord.objects.none()

    def get_permissions(self):
        if self.action == "destroy":
            permission_classes=[IsAdmin]
        elif self.action in ["create", "update", "partial_update"]:
            permission_classes= [IsAdminOrDoctor]
        elif self.action in ["list", "retrieve"]:
            permission_classes= [CanViewMedical_record]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

