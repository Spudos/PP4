from django.contrib import admin
from .models import Booking, Sessions, Appointments
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('session_type', 'user', 'created_on')
    search_fields = ['session_type', 'user']
    list_filter = ('user', 'created_on')
    summernote_field = ('notes')


@admin.register(Sessions)
class SessionsAdmin(admin.ModelAdmin):
    list_display = ('session_type', 'Description',
                    'excerpt', 'created_on', 'image')
    list_filter = ('session_type', 'created_on')
    summernote_field = ('session_type', 'Description', 'excerpt')


@admin.register(Appointments)
class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('appointment_type', 'date_time')
