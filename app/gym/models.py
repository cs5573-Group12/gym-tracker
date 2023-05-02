from django.utils import timezone
from datetime import datetime, timedelta
from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
MALE = 'M'
FEMALE = 'F'
OTHER = 'O'

GENDER_CHOICES = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
]

# employee
class Employee(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  phone = models.CharField(max_length=50, default="", blank=True)
  email = models.CharField(max_length=50, default="", blank=True)
  age = models.IntegerField(default=18, blank=True)
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=OTHER)
  startdate = models.DateTimeField(default=timezone.now)

  def __str__(self):
      return self.name