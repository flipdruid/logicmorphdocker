from accounts.models.user import User
from django.test import TestCase


class TestUser(TestCase):
    def setUp(self):
        self.user=User.objects.create(
            username="userJuan",
            password="secretnijuan",
            first_name="Juan",
            last_name="Delacruz",
            email="flipdruid@yahoo.com"
        )
        
    def test_username_str(self):
        self.username = "userJuan"
        self.assertEqual(str(self.username), str(self.user.username))
    
    def test_password_str(self):
        self.password = "secretnijuan"
        self.assertEqual(str(self.password), str(self.user.password))

    def test_first_name_str(self):
        self.first_name = "Juan"
        self.assertEqual(str(self.first_name), str(self.user.first_name))

    def test_last_name_str(self):
        self.last_name = "Delacruz"
        self.assertEqual(str(self.last_name), str(self.user.last_name))
    
    def test_email_str(self):
        self.email = "flipdruid@yahoo.com"
        self.assertEqual(str(self.email), str(self.user.email))
            