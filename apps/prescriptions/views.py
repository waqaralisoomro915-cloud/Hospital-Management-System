from rest_framework import viewsets
from rest_framework.decorators import permission_classes

from .serializers import PrescriptionSerializer
from .models import Prescription
from ..accounts.models import User
from ..accounts.permissions import (IsAdminOrDoctor,CanviewPrescription)
from rest_framework.permissions import IsAuthenticated

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role  in [
            User.Role.NURSE,
            User.Role.ADMIN,
        ]:
            return Prescription.objects.all()
        elif user.role == User.Role.PATIENT:
            return Prescription.objects.filter(patient_user=user)
        elif user.role == User.Role.DOCTOR:
            return Prescription.objects.filter(doctor_user=user)

        return Prescription.objects.none()
    def get_permissions(self):
        if self.action == "destroy":
            permission_classes =[IsAdminOrDoctor]
        elif self.action in ["create", "update", "partial_update"]:
            permission_classes =[IsAdminOrDoctor]
        elif self.action in ["list", "retrieve"]:
            permission_classes=[CanviewPrescription]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


