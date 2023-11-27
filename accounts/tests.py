from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from .forms import CustomUserCreationForm
from .views import SignupPageView


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="will", email="will@test.com", password="testpass123"
        )
        self.assertEqual(user.username, "will")
        self.assertEqual(user.email, "will@test.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(
            username="admin", email="admin@test.com", password="adminpass123"
        )
        self.assertEqual(superuser.username, "admin")
        self.assertEqual(superuser.email, "admin@test.com")
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
