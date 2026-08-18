from .views import PrescriptionViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('prescriptions', PrescriptionViewSet,basename='prescriptions')
urlpatterns = router.urls