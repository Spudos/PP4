from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

SESSION_TYPE = (
    ("Gym", "Gym"),
    ("Strength", "Strength"),
    ("Cardio", "Cardio"),
    ("Nutrition", "Nutrition"),
    ("Motivation", "Motivation"),
    ("Weight Loss", "Weight Loss")
)


class Appointments(models.Model):
    appointment_type = models.TextField(default='General')
    date_time = models.DateTimeField()
    booking_id = models.OneToOneField('Booking',
                                      on_delete=models.SET_NULL,
                                      null=True, blank=True)


class Booking(models.Model):
    session_type = models.TextField(choices=SESSION_TYPE, default='Gym')
    notes = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.OneToOneField(Appointments,
                                       on_delete=models.DO_NOTHING)
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.appointment_id:
            appointment = Appointments.objects.get(pk=self.appointment_id)
            appointment.booking = self
            appointment.save()
        super(Booking, self).save(*args, **kwargs)


class Sessions(models.Model):
    session_type = models.TextField(choices=SESSION_TYPE, default='Gym')
    Description = models.TextField()
    excerpt = models.TextField()
    image = CloudinaryField('image', default='none')
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
