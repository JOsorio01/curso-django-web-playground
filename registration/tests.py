from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User


class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test_user', 'test_user@test.com', 'test_passwd1')


    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test_user').exists()
        self.assertEqual(exists, True)
