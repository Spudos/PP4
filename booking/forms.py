from django import forms
from .models import Booking, Appointments
from datetime import date
from django.db.models import Q


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['session_type', 'notes', 'user', 'appointment']


class BookingEditForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['session_type', 'notes', 'appointment']

    def __init__(self, *args, **kwargs):
        super(BookingEditForm, self).__init__(*args, **kwargs)

        if self.instance.appointment:
            self.initial['appointment'] = self.instance.appointment.id

        current_date = date.today()
        self.fields['appointment'].queryset = Appointments.objects.filter(
            Q(booking__isnull=True) | Q(booking=self.instance)).filter(
            date_time__gt=current_date).order_by("date_time")
        self.fields['appointment'
                    ].label_from_instance = lambda obj: obj.date_time.strftime(
                    '%B %d, %Y, %-I %p')
