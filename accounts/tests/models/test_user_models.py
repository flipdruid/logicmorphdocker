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
        return
    
    def tearDown(self):
        self.user=None
        
    def test_create_user(self):
        self.username = "userJuan"
        self.assertEqual(str(self.username), str(self.user.username))
        self.password = "secretnijuan"
        self.assertEqual(str(self.password), str(self.user.password)) 
        self.first_name = "Juan"
        self.assertEqual(str(self.first_name), str(self.user.first_name)) 
        self.last_name = "Delacruz"
        self.assertEqual(str(self.last_name), str(self.user.last_name))
        self.email = "flipdruid@yahoo.com"
        self.assertEqual(str(self.email), str(self.user.email))