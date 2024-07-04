from django.urls import path
from .views import MedicalPrescriptionCreateAPIView

urlpatterns = [
    path('api/medical-prescriptions/', MedicalPrescriptionCreateAPIView.as_view(), name='medical-prescription-create'),
]