from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

TYPE = ((0, "Gym"),
        (1, "Strength"),
        (2, "Cardio"),
        (3, "Nutrition"),
        (4, "Motivation"),
        (5, "Weight Loss"))

class Booking(models.Model):
  type = models.IntegerField(choices=TYPE, default=0)
  notes = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  cancelled = models.BooleanField(default=False)
  booking_date_time = models.DateTimeField()
  last_update = models.DateTimeField(auto_now=True)
  created_on = models.DateTimeField(auto_now_add=True)
  
class Sessions(models.Model):
  type = models.IntegerField(choices=TYPE, default=0)
  Description = models.TextField(max_length=200, unique=True)
  excerpt = models.TextField(max_length=50, unique=True)
  image = CloudinaryField('image', default='none')
  last_update = models.DateTimeField(auto_now=True)
  created_on = models.DateTimeField(auto_now_add=True)

