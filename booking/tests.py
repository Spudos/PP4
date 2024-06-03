from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Sessions, Appointments, Booking

class BookingTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', first_name='test', last_name='testy', password='testpassword')
        self.session = Sessions.objects.create(session_type='Motivation')
        self.appointment = Appointments.objects.create(
            date_time='2024-09-01 10:00:00')
        appointment1 = Appointments.objects.create(
            date_time='2024-09-01 10:00:00')
        self.booking = Booking.objects.create(
            user=self.user, session_type=self.session,
            appointment=self.appointment)
        self.url = reverse('booking_edit', kwargs={'pk': self.booking.pk})

    def test_booking_page(self):
        response = self.client.get(reverse('booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')

    def test_booking_form_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('booking_form'), {'session_type': self.session.id})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking_form.html')
    
    def test_booking_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('booking_success', kwargs={'booking_id': self.booking.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking_success.html')

    def test_get_edit_form(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking_edit.html')
