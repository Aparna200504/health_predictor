from django.db import models
from django.core.validators import MinValueValidator, EmailValidator
from datetime import date

class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    glucose = models.FloatField(validators=[MinValueValidator(0.1)])      # mg/dL
    haemoglobin = models.FloatField(validators=[MinValueValidator(0.1)])  # g/dL
    cholesterol = models.FloatField(validators=[MinValueValidator(0.1)])  # mg/dL
    remarks = models.TextField(blank=True, default='')

    def __str__(self):
        return self.full_name
