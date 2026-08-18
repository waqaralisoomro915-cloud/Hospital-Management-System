
from .views import HospitalizationViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register("hospitalization", HospitalizationViewSet, basename="hospitalization")
urlpatterns = router.urls
