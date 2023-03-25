from django.db import models

# Create your models here.

class BloodPressure(models.Model):

    user = models.ForeignKey('users.User',on_delete=models.CASCADE)
    systlic = models.PositiveIntegerField()
    diastolic = models.PositiveIntegerField()
    pulse = models.PositiveIntegerField()
    examination_datetime = models.DateTimeField()
    notes = models.TextField(null=True,blank=True)
