from django.test import TestCase
from datetime import datetime
from app.models.developer import Developer
from app.models.profile import Profile
from app.models.project import Project
from app.models.client import Client
from accounts.models.user import User



class TestDeveloperModels(TestCase):

    def create_user(self):
        user = User.objects.create(**self.user_credentials)
        return user

    def create_profile(self):
        self.profile=Profile.objects.create(
            user=self.user,
            avatar="logo.jpg",
            is_logicmorph_staff =True,
            is_dark_theme = True, 
        ) 
        return self.profile

    def create_client(self):
        self.client=Client.objects.create(
            profile = self.profile,
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

    

    def create_developer(self):
        self.developer=Developer.objects.create(
        project=self.project,
        profile=self.profile,
        role = "Developer",
        state = "New"        
        )
        self.developerID = self.developer.id
        return self.developer

    def setUp(self):        
        self.user_credentials = {'username': 'john', 'password': 'john_doe'}
        self.user=self.create_user()
        self.profile=self.create_profile()
        self.client=self.create_client()
        self.client=self.create_project()            
        self.developer=self.create_developer()

    def tearDown(self):
        self.user=None
        self.client=None
        self.project=None
        self.profile=None
        self.developer=None

    def test_create_developer(self):
        self.assertEqual(self.developer.project, self.project)  
        self.assertEqual(self.developer.profile, self.profile)        
        self.assertEqual(self.developer.role, "Developer")
        self.assertEqual(self.developer.state, "New")

    def test_read_developer(self):
        self.getDeveloper = Developer.objects.get(id=self.developerID)
        self.assertEqual(self.getDeveloper.project, self.project)  
        self.assertEqual(self.getDeveloper.profile, self.profile)        
        self.assertEqual(self.getDeveloper.role, "Developer")
        self.assertEqual(self.getDeveloper.state, "New")

    def test_update_developer(self):
        self.getDeveloper = Developer.objects.get(id=self.developerID)
        self.getDeveloper.role="New Developer"
        self.getDeveloper.state="New State"
        self.assertEqual(self.getDeveloper.project, self.project)  
        self.assertEqual(self.getDeveloper.profile, self.profile)        
        self.assertEqual(self.getDeveloper.role, "New Developer")
        self.assertEqual(self.getDeveloper.state, "New State")

    def test_delete_developer(self):
        Developer.objects.get(id=self.developerID).delete()
        counts = Developer.objects.filter(id=self.developerID).count()
        self.assertEqual(counts, 0)