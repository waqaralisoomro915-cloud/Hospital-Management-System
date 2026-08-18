from rest_framework import viewsets
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
            User.Role.Nurse,
            User.Role.Admin,
        ]:
            return PrescriptionMedicine.objects.all()
        elif user.role == User.Role.Patient:
            return PrescriptionMedicine.objects.filter(prescription__patient_user=user)
        elif user.role == User.Role.Doctor:
            return PrescriptionMedicine.objects.filter(prescription__doctor_user=user)

        return PrescriptionMedicine.objects.none()
    def get_permissions(self):
        if self.action == "destroy":
            return [IsAdmin]
        elif self.action in ["create", "update", "partial_update"]:
            return [IsAdminOrDoctor]
        elif self.action in ["list", "retrieve"]:
            return [CanviewPrescription]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


