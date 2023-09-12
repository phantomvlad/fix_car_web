from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()

        user= User.objects.create_user(username='Vlad', email='mmvlad99@mail.ru', password='123qwe', car='micra')
        self.assertEqual(user.email, 'mmvlad99@mail.ru')
        self.assertNotEqual(user.email, 'mmvlad99@nail.ru')
        self.assertEqual(user.username, 'Vlad')
        self.assertNotEqual(user.email, 'vlad')
        self.assertEqual(user.car, 'micra')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)