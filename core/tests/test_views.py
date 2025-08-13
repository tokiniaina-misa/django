from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class CoreViewsTest(TestCase):
    def test_frontpage(self):
        response = self.client.get(reverse("frontpage"))
        self.assertEqual(response.status_code, 200)

    def test_signup_post(self):
        response = self.client.post(reverse("signup"), {
            "username": "newuser",
            "password1": "StrongPass123",
            "password2": "StrongPass123"
        })
        self.assertEqual(response.status_code, 302)  # Redirection après signup
        self.assertTrue(User.objects.filter(username="newuser").exists())
