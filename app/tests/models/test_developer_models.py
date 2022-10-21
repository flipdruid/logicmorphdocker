from django.test import TestCase
from datetime import datetime
from accounts.models import profile
from app.models.developer import Developer
from app.models.profile import Profile
from app.models.project import Project
from app.models.client import Client
from accounts.models.user import User
from accounts.tests.models.test_user_models import TestUser
class TestLeadModels(TestCase):


    def setUp(self):

        self.user=TestUser.setUp(self)

        self.client=Client.objects.create(
            business_name='Logic Morph',
            business_logo="logo.png",
            address="Philippines",
            telephone_no="123456",
            position ="Developer"
        )   
       
        self.project=Project.objects.create(
            name= "Philip",
            state="New",
            client=self.client,
            created_at=datetime.today().strftime('%Y-%m-%d'),
            updated_at=datetime.today().strftime('%Y-%m-%d')
        )

        self.profile=Profile.objects.create(
            user=self.user,
            avatar="logo.jpg",
            is_logicmorph_staff =True,
            is_dark_theme = True, 
        )   

        self.developer=Developer.objects.create(
        project=self.project,
        profile=self.profile,
        role = "Developer",
        state = "New"
        
        )

    def tearDown(self):
        self.user=None
        self.project=None
        self.profile=None
        self.developer=None

    def test_create_developer(self):
        self.assertEqual(self.developer.project, self.project)  
        self.assertEqual(self.developer.profile, self.profile)        
        self.assertEqual(self.developer.role, "Developer")
        self.assertEqual(self.developer.state, "New")