from django.db import models
from django.contrib.auth.models import User

class MedicalPrescription(models.Model):
    doctor_id = models.IntegerField()
    patient_id = models.IntegerField()
    medication_id = models.IntegerField()
    description = models.TextField()
    dose = models.CharField(max_length=255)
    prescription_file = models.FileField()