from django.test import TestCase
from django.urls import reverse
from django.core import mail
from .forms import ContactForm
from .views import ContactView

class ContactViewTests(TestCase):
    def test_contact_form_submission(self):
        # Create a contact form instance with valid data
        form_data = {
            "email": "test@example.com",
            "subject": "Test Subject",
            "message": "Test Message",
        }
        form = ContactForm(data=form_data)

        # Submit the form
        response = self.client.post(reverse("contact"), data=form_data)

        # Check that the form submission was successful
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("success"))

        # Check that the email was sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Received contact form submission")
        self.assertEqual(mail.outbox[0].from_email, "spudos16@gmail.com")
        self.assertEqual(mail.outbox[0].to, ["spudos16@gmail.com", "test@example.com"])
