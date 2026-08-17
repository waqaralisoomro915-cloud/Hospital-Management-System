from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Nurse
from .serializers import NurseSerializer
from ..accounts.permissions import (
    CanViewNurse,
    IsAdmin,
    IsAdminOrDoctor,
)

class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    def get_queryset(self):
        user = self.request.user

        if user.role in [
            user.Role.ADMIN,
            user.Role.DOCTOR,
        ]:
            return Nurse.objects.all()

        if user.role == user.Role.NURSE:
            return Nurse.objects.filter(user=user)

        return Nurse.objects.none()

    def get_permissions(self):

        if self.action == "destroy":
            permission_classes = [IsAdmin]

        elif self.action in ["create", "update", "partial_update"]:
            permission_classes = [IsAdminOrDoctor]

        elif self.action in ["list", "retrieve"]:
            permission_classes = [CanViewNurse]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
