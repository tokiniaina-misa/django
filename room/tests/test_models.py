from django.test import TestCase
from django.contrib.auth.models import User
from room.models import Room, Message

class RoomModelTest(TestCase):
    def test_create_room(self):
        room = Room.objects.create(name="General", slug="general")
        self.assertEqual(str(room.name), "General")
        self.assertEqual(room.slug, "general")

class MessageModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.room = Room.objects.create(name="General", slug="general")

    def test_create_message(self):
        message = Message.objects.create(room=self.room, user=self.user, content="Hello")
        self.assertEqual(message.content, "Hello")
        self.assertEqual(message.room, self.room)
        self.assertEqual(message.user, self.user)
