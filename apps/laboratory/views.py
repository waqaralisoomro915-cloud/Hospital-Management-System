from re import search

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets


from ..paginations import CustomPagination
from .models import Laboratory
from.serializers import LaboratorySerializer
from ..accounts.permissions import (CanViewLaboratory,IsAdmin,IsAdminOrDoctor)
from rest_framework.permissions import IsAuthenticated
class LaboratoryViewSet(viewsets.ModelViewSet):
    queryset = Laboratory.objects.all()
    serializer_class = LaboratorySerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,OrderingFilter,SearchFilter,)
    filterset_fields=["status","test_type","doctor", "patient"]
    search_fields = ["name","status","test_type","doctor", "patient"]
    ordering_fields=['test_date','created_at','status']


    def get_queryset(self):
        user = self.request.user

        if user.role in [
            user.Role.ADMIN,
            user.Role.NURSE,
        ]:
            return Laboratory.objects.all()
        elif user.role == user.Role.PATIENT:
            return Laboratory.objects.filter(patient__user=user)
        elif user.role == user.Role.DOCTOR:
            return Laboratory.objects.filter(doctor__user=user)
        return Laboratory.objects.none()


    def get_permissions(self):

        if self.action == "destroy":
            permission_classes = [IsAdmin]

        elif self.action in ["create", "update", "partial_update"]:
            permission_classes = [IsAdminOrDoctor]

        elif self.action in ["list", "retrieve"]:
            permission_classes = [CanViewLaboratory]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]