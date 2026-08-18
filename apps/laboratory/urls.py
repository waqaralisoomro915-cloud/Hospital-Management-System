from .views import  LaboratoryViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('laboratory', LaboratoryViewSet, basename='laboratory')
urlpatterns = router.urls