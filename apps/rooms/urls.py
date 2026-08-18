from django.urls import path
from .views import RoomViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("room", RoomViewSet, basename="room")

urlpatterns = router.urls