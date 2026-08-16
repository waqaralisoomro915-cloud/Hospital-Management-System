
from .views import DoctorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("doctor", DoctorViewSet, basename="doctor")

urlpatterns = router.urls