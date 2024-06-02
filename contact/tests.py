from django.test import TestCase
from django.urls import reverse
from django.core import mail
from contact.forms import ContactForm
from contact.views import ContactView


class ContactViewTest(TestCase):
    def test_contact_form_submission(self):
        form_data = {
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test Message',
        }
        response = self.client.post(reverse('contact'), form_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject,
                         'Received contact form submission')
        self.assertIn('Test Message', mail.outbox[0].body)
