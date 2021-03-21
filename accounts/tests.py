from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import CustomUser


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='tester',
            email='tester@example.com',
            password='testpassword'
        )
        self.assertEqual(user.username, 'tester')
        self.assertEqual(user.email, 'tester@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='supertest',
            email='supertest@example.com',
            password='supertestpassword'
        )
        self.assertEqual(user.username, 'supertest')
        self.assertEqual(user.email, 'supertest@example.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class AbstractUserModelTests(TestCase):
    def test_create_user(self):
        User = CustomUser
        user = User.objects.create_user(
            username='tester',
            email='tester@example.com',
            password='testpassword'
        )
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.username, 'tester')
        self.assertEqual(user.email, 'tester@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = CustomUser
        user = User.objects.create_superuser(
            username='supertest',
            email='supertest@example.com',
            password='supertestpassword'
        )
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.username, 'supertest')
        self.assertEqual(user.email, 'supertest@example.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
