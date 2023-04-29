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

# Create user and save to the database
# user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# Update fields and then save again
# user.first_name = 'Tyrone'
# user.last_name = 'Citizen'
# user.save()

# employee
class Employee(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  phone = models.CharField(max_length=50, default="", blank=True)
  email = models.CharField(max_length=50, default="", blank=True)
  age = models.IntegerField(default=0, blank=True)
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=OTHER)
  startdate = models.DateField(default=timezone.now)

  def __str__(self):
      return self.name

# member

# guest
class Guest(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  phone = models.CharField(max_length=50, default="", blank=True)
  email = models.CharField(max_length=50, default="", blank=True)
  age = models.IntegerField(default=0, blank=True)
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=OTHER)
  date = models.DateField(default=timezone.now)
  price = models.IntegerField(default=10, blank=True)

  def __str__(self):
      return self.name
    
# entry
class GuestEntry(models.Model):
  id = models.AutoField(primary_key=True)
  guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
  date =models.DateField(default=timezone.now)

  def __str__(self):
      return self.guest.name + " " + self.entrydate + " " + self.entrytime