from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from booking.models import Booking, Appointments
from django.utils import timezone

class UserAccountTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_user_account_view(self):
        response = self.client.get(reverse('user_account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_account.html')

    def test_user_past_bookings(self):
        appointment = Appointments.objects.create(date_time=datetime(2024, 2, 1, 0, 0))
        past_booking = Booking.objects.create(user=self.user, appointment=appointment)
        response = self.client.get(reverse('user_account'))
        self.assertEqual(response.status_code, 200)
        
        user_past_bookings = response.context['user_past_bookings']
        self.assertIn(past_booking.pk, [obj.pk for obj in user_past_bookings])

    def test_user_future_bookings(self):
        appointment = Appointments.objects.create(date_time=datetime(2024, 8, 1, 0, 0))
        future_booking = Booking.objects.create(user=self.user, appointment=appointment)
        response = self.client.get(reverse('user_account'))
        self.assertEqual(response.status_code, 200)
        
        user_future_bookings = response.context['user_future_bookings']
        self.assertIn(future_booking.pk, [obj.pk for obj in user_future_bookings])

    def test_delete_booking(self):
        appointment = Appointments.objects.create(date_time=timezone.now())  # Create the related Appointment
        booking = Booking.objects.create(user=self.user, appointment=appointment)  # Create the Booking with the related Appointment
        response = self.client.post(reverse('delete_booking', args=[booking.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user_account'))
        self.assertFalse(Booking.objects.filter(id=booking.id).exists())
