from django.test import TestCase
from datetime import datetime
from app.models import Post
from accounts.models.user import User
from app.models.profile import Profile

class TestPostModels(TestCase):    

    def setUp(self):        

        self.user=User.objects.create(
            username="userJuan",
            password="secretnijuan",
            first_name="Juan",
            last_name="Delacruz",
            email="flipdruid@yahoo.com"
        )
        
        self.profile=Profile.objects.create(
            user=self.user,
            avatar="logo.jpg",
            is_logicmorph_staff =True,
            is_dark_theme = True, 
        )  

    def test_user_profile_object(self):
        self.assertEqual(self.profile.user, self.user)

    def test_avatar_img(self):
        self.assertEqual(self.profile.avatar, "logo.jpg")

    def test_is_logicmorph_staff_bol(self):
        self.assertEqual(self.profile.is_logicmorph_staff, True)
    
    def test_is_dark_theme_bol(self):
        self.assertEqual(self.profile.is_dark_theme, True)

    
            