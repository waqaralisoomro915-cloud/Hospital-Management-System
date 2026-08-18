from .views import PrescriptionMedicineViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('prescriptionMedicine', PrescriptionMedicineViewSet,basename='prescriptionMedicine')
urlpatterns = router.urls