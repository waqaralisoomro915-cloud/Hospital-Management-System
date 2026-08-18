from .models import Hospitalization
from rest_framework import viewsets
from ..accounts.permissions import (IsAdminOrDoctor,IsAdmin,CanViewHospitalization)
from rest_framework.permissions import IsAuthenticated

from .serializers import HospitalizationSerializer


class HospitalizationViewSet(viewsets.ModelViewSet):
    queryset = Hospitalization.objects.all()
    serializer_class = HospitalizationSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role in [
            user.Role.ADMIN,
            user.Role.DOCTOR,
            user.Role.NURSE,
        ]:
            return Hospitalization.objects.all()
        elif user.role == user.Role.PATIENT:
            return Hospitalization.objects.filter(patient__user=user)
        return Hospitalization.objects.none()


    def get_permissions(self):

        if self.action == "destroy":
            permission_classes = [IsAdmin]

        elif self.action in ["create", "update", "partial_update"]:
            permission_classes = [IsAdminOrDoctor]

        elif self.action in ["list", "retrieve"]:
            permission_classes = [CanViewHospitalization]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]