from ..accounts.permissions import (
IsAdmin,CanViewRoom,IsAdminOrDoctor
)
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets
from .models import Room
from .serializers import RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role in [
            user.Role.ADMIN,
            user.Role.DOCTOR,
            user.Role.NURSE,
        ]:
            return Room.objects.all()
        return Room.objects.none()


    def get_permissions(self):

        if self.action == "destroy":
            permission_classes = [IsAdmin]

        elif self.action in ["create", "update", "partial_update"]:
            permission_classes = [IsAdminOrDoctor]

        elif self.action in ["list", "retrieve"]:
            permission_classes = [CanViewRoom]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]