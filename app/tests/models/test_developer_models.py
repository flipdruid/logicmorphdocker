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

    def create_user(self):
        user = User.objects.create(**self.user_credentials)
        return user

    # def create_user(self):
    #     self.user=User.objects.create(
    #         username="userJuan",
    #         password="secretnijuan",
    #         first_name="Juan",
    #         last_name="Delacruz",
    #         email="flipdruid@yahoo.com"
    #     )
    #     return self.user

    def create_client(self):
        self.client=Client.objects.create(
            business_name='Logic Morph',
            business_logo="logo.png",
            address="Philippines",
            telephone_no="123456",
            position ="Developer"
        )   
        return self.client

    
    def create_project(self):
        self.project=Project.objects.create(
            name= "Philip",
            state="New",
            client=self.client,
            created_at=datetime.today().strftime('%Y-%m-%d'),
            updated_at=datetime.today().strftime('%Y-%m-%d')
        )
        return self.project

    def create_profile(self):
        self.profile=Profile.objects.create(
            user=self.user,
            avatar="logo.jpg",
            is_logicmorph_staff =True,
            is_dark_theme = True, 
        ) 
        return self.profile

    def create_developer(self):
        self.developer=Developer.objects.create(
        project=self.project,
        profile=self.profile,
        role = "Developer",
        state = "New"
        
        )
        return self.developer

    def setUp(self):        
        self.user_credentials = {'username': 'john', 'password': 'john_doe'}
        self.user=self.create_user(**self.user_credentials)
        
        # self.user=self.create_user()
        self.client=self.create_client()
        self.project=self.create_project()
        self.profile=self.create_profile()
        self.developer=self.create_developer()

    def tearDown(self):
        self.user=None
        self.clien=None
        self.project=None
        self.profile=None
        self.developer=None

    def test_create_developer(self):
        self.assertEqual(self.developer.project, self.project)  
        self.assertEqual(self.developer.profile, self.profile)        
        self.assertEqual(self.developer.role, "Developer")
        self.assertEqual(self.developer.state, "New")