from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

SESSION_TYPE = (("Gym", "Gym"),
        ("Strength", "Strength"),
        ("Cardio", "Cardio"),
        ("Nutrition", "Nutrition"),
        ("Motivation", "Motivation"),
        ("Weight Loss", "Weight Loss"))

class Booking(models.Model):
  session_type = models.TextField(choices=SESSION_TYPE, default='Gym')
  notes = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  cancelled = models.BooleanField(default=False)
  booking_date_time = models.DateTimeField()
  last_update = models.DateTimeField(auto_now=True)
  created_on = models.DateTimeField(auto_now_add=True)

class Sessions(models.Model):
  session_type = models.TextField(choices=SESSION_TYPE, default='Gym')
  Description = models.TextField()
  excerpt = models.TextField()
  image = CloudinaryField('image', default='none')
  last_update = models.DateTimeField(auto_now=True)
  created_on = models.DateTimeField(auto_now_add=True)

