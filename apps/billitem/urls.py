from .views import BillItemViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('billitem', BillItemViewSet,basename='billitem')
urlpatterns = router.urls