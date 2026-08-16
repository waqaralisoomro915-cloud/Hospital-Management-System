from rest_framework import viewsets
from .serializers import DepartmentSerializer
from .models import Department
from ..accounts.permissions import (IsPatient,IsNurse,IsDoctor,IsAdmin,CanViewDepartment)



class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = [IsAdmin]
        else:
            permission_classes = [CanViewDepartment]

        return [permission() for permission in permission_classes]
