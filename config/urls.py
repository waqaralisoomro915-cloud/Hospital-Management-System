from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.accounts.urls')),
    path('', include('apps.billing.urls')),
    path('', include('apps.departments.urls')),
    path('', include('apps.doctors.urls')),
    path('', include('apps.hospitalization.urls')),
    path('', include('apps.laboratory.urls')),
    path('', include('apps.medical_records.urls')),
    path('', include('apps.patients.urls')),
    path('', include('apps.prescriptions.urls')),

    # Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
]