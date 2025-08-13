from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from room.models import Room

class RoomViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.room = Room.objects.create(name="General", slug="general")

    def test_rooms_view_requires_login(self):
        response = self.client.get(reverse("rooms"))
        self.assertEqual(response.status_code, 302)  # redirection login

    def test_rooms_view_authenticated(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("rooms"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "General")

    def test_room_detail_view(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("room", args=["general"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "General")
