from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from ..accounts.models import User
from .serializers import DoctorSerializer
from .models import Doctor
from ..accounts.permissions import CanViewDoctor
from ..paginations import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    filterset_fields = ('specialization','experience','qualification',)
    search_fields = ('specialization',)
    ordering_fields = ('specialization','experience','qualification',)
    ordering =["created_at"]




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