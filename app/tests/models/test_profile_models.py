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

    def test_create_user_profile(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.avatar, "logo.jpg")
        self.assertEqual(self.profile.is_logicmorph_staff, True)
        self.assertEqual(self.profile.is_dark_theme, True)

    def test_read_user_profile(self):
        getUserProfile = Profile.objects.get(user=self.user)
        self.assertEqual(getUserProfile.user, self.user)
        self.assertEqual(getUserProfile.avatar, "logo.jpg")
        self.assertEqual(getUserProfile.is_logicmorph_staff, True)
        self.assertEqual(getUserProfile.is_dark_theme, True)

    def test_update_user_profilet(self):
        getUserProfile = Profile.objects.get(user=self.user)
        getUserProfile.avatar="logo2.jpg"
        getUserProfile.is_logicmorph_staff=False
        getUserProfile.is_dark_theme=False
        getUserProfile.save()
        self.assertEqual(getUserProfile.user, self.user)
        self.assertEqual(getUserProfile.avatar, "logo2.jpg")
        self.assertEqual(getUserProfile.is_logicmorph_staff, False)
        self.assertEqual(getUserProfile.is_dark_theme, False)

    def test_delete_user_profilet(self):
        Profile.objects.get(user=self.user).delete()
        counts = Profile.objects.filter(user=self.user).count()
        self.assertEqual(counts, 0)