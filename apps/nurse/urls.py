from django.urls import path
from .views import NurseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("nurse", NurseViewSet, basename="nurse")

urlpatterns = router.urls