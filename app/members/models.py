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
def one_year_from_now():
  return timezone.now() + timedelta(days=365)
# Create your models here.
class Member(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  phone = models.CharField(max_length=50, default="", blank=True)
  email = models.CharField(max_length=50, default="", blank=True)
  age = models.IntegerField(default=18, blank=True)
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=OTHER)
  plan = models.CharField(max_length=50, default="", blank=True)
  registered_by = models.ForeignKey(User, on_delete=models.CASCADE)
  joindate = models.DateTimeField(default=timezone.now)
  expiredate = models.DateTimeField(default=one_year_from_now)
  initialamount = models.IntegerField(default=40, blank=True)

  def __str__(self):
      return self.name
  
  
class MemberEntry(models.Model):
  id = models.AutoField(primary_key=True)
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  date = models.DateTimeField(default=timezone.now)
  checked_in_by = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
      return self.member.name + " " + self.entrydate + " " + self.entrytime
