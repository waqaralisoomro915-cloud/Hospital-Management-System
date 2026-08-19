from rest_framework import viewsets
from rest_framework.decorators import permission_classes

from .serializers import PrescriptionMedicineSerializer
from .models import PrescriptionMedicine
from ..accounts.models import User
from ..accounts.permissions import (IsAdminOrDoctor,CanviewPrescription,IsAdmin)
from rest_framework.permissions import IsAuthenticated


class PrescriptionMedicineViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionMedicine.objects.all()
    serializer_class = PrescriptionMedicineSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role  in [
            User.Role.NURSE,
            User.Role.ADMIN,
        ]:
            return PrescriptionMedicine.objects.all()
        elif user.role == User.Role.PATIENT:
            return PrescriptionMedicine.objects.filter(prescription__patient_user=user)
        elif user.role == User.Role.DOCTOR:
            return PrescriptionMedicine.objects.filter(prescription__doctor_user=user)

        return PrescriptionMedicine.objects.none()
    def get_permissions(self):
        if self.action == "destroy":
            permission_classes=[IsAdmin]
        elif self.action in ["create", "update", "partial_update"]:
            permission_classes=[IsAdminOrDoctor]
        elif self.action in ["list", "retrieve"]:
            permission_classes=[CanviewPrescription]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


