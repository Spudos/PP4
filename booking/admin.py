from django.contrib import admin
from .models import Booking, Sessions
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('type', 'user', 'cancelled', 'booking_date_time', 'created_on')
    search_fields = ['type', 'user']
    list_filter = ('user', 'cancelled', 'created_on')
    summernote_field = ('notes')
    
@admin.register(Sessions)
class SessionsAdmin(admin.ModelAdmin):
    list_display = ('session_type', 'Description', 'excerpt', 'created_on', 'image')
    list_filter = ('session_type', 'created_on')
