from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from ..accounts.models import User
from .serializers import DoctorSerializer
from .models import Doctor
from ..accounts.permissions import CanViewDoctor


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


    def get_queryset(self):
        user = self.request.user

        if user.role == User.Role.DOCTOR:
            return Doctor.objects.filter(user=user)

        return Doctor.objects.all()

    def get_permissions(self):
        if self.action in ['create','update', 'partial_update','destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [CanViewDoctor]

        return [permission() for permission in permission_classes]