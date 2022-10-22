from django.test import TestCase
from datetime import datetime
from app.models import Post
from accounts.models.user import User
from app.models.profile import Profile

class TestProfileModels(TestCase):   

    def create_user(self):
        self.user=User.objects.create(
            username="userJuan",
            password="secretnijuan",
            first_name="Juan",
            last_name="Delacruz",
            email="flipdruid@yahoo.com"
        )
        return self.user 

    def create_profile(self):
        self.profile=Profile.objects.create(
            user=self.user,
            avatar="logo.jpg",
            is_logicmorph_staff =True,
            is_dark_theme = True, 
        )  
        return self.profile

    def setUp(self):        
        self.user=self.create_user()
        self.profile=self.create_profile()       
        

    def tearDown(self):
        self.user=None
        self.profile=None

    def test_user_profile_object(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.avatar, "logo.jpg")
        self.assertEqual(self.profile.is_logicmorph_staff, True)
        self.assertEqual(self.profile.is_dark_theme, True)