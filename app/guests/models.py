from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User

MALE = 'M'
FEMALE = 'F'
OTHER = 'O'

GENDER_CHOICES = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
]

# Create your models here.
class Guest(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  phone = models.CharField(max_length=50, default="", blank=True)
  email = models.CharField(max_length=50, default="", blank=True)
  age = models.IntegerField(default=18, blank=True)
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=OTHER)
  date = models.DateTimeField(default=timezone.now)
  price = models.IntegerField(default=10, blank=True)
  checked_in_by = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
      return self.name