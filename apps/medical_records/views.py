from rest_framework import viewsets
from ..paginations import CustomPagination
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer
from ..accounts.models import User
from ..accounts.permissions import (IsAdmin,IsAdminOrDoctor,CanViewMedical_record)
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ["patient", "doctor", "hospitalization"]
    search_fields = ["patient", "doctor"]
    ordering_fields = ["record_date", "created_at", "updated_at"]
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

