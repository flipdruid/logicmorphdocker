from accounts.models.user import User
from django.test import TestCase, Client

class TestUser(TestCase):
    def setUp(self):
        self.user=User.objects.create(
            username="userJuan",
            password="secretnijuan",
            first_name="Juan",
            last_name="Delacruz",
            email="flipdruid@yahoo.com"
        )
        client=Client()
    def tearDown(self):
        self.user=None
        
    def test_create_user(self):
        self.assertEqual(str(self.user.username), "userJuan" )
        self.assertEqual(str(self.user.password), "secretnijuan") 
        self.assertEqual(str(self.user.first_name), "Juan") 
        self.assertEqual(str(self.user.last_name), "Delacruz")
        self.assertEqual(str(self.user.email), "flipdruid@yahoo.com")