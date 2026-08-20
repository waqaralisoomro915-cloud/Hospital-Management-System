from rest_framework import viewsets
from .serializers import DepartmentSerializer
from .models import Department
from ..accounts.permissions import (IsPatient,IsNurse,IsDoctor,IsAdmin,CanViewDepartment)
from ..paginations import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    filterset_fields=('name','location',)
    search_fields=('name','location',)
    ordering_fields = ('name','location','phone_number',)


    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = [IsAdmin]
        else:
            permission_classes = [CanViewDepartment]

        return [permission() for permission in permission_classes]
