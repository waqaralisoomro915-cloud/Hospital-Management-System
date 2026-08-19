from .views import MedicalRecord, MedicalRecordViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('MedicalRecord', MedicalRecordViewSet,basename='MedicalRecord')
urlpatterns = router.urls