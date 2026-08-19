from .views import BillingViewSet
from rest_framework import viewsets, routers

router = routers.DefaultRouter()
router.register(r'patient', BillingViewSet,basename='patient')
urlpatterns = router.urls