from tarfile import CONTTYPE
from unicodedata import name
from django.test import TestCase
from datetime import datetime
from app.models.client import Client
from app.models.project import Project
from app.models.profile import Profile
from accounts.models.user import User

class TestProjectModels(TestCase):

    def create_client(self):

        self.credentials = {
            'username': 'userJuan',
            'password': 'secretnijuan',
            'first_name':'Juan',
            'last_name' : 'Delacruz',
            'email': 'testemail@email.com',
            'is_active': 'True'
            }

        self.user = User.objects.create(**self.credentials)

        self.profile = Profile.objects.create(
            user = self.user,
            avatar = 'avatar.jpg',
            is_logicmorph_staff = False,
            is_dark_theme = False
        )

        self.client=Client.objects.create(
            business_name='Logic Morph',
            business_logo="logo.png",
            address="Philippines",
            telephone_no="123456",
            position ="Developer",
            profile = self.profile
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
        self.created_at=self.project.created_at
        self.updated_at=self.project.updated_at
        self.projectID = self.project.id
        return self.project
    
    def setUp(self):
        self.client=self.create_client()       
        self.project=self.create_project()

        
    
    def tearDown(self):
        self.client=None
        self.project=None
        
    def test_create_project(self):
        self.assertEqual(self.project.name, "Philip")
        self.assertEqual(self.project.state, "New")
        self.assertEqual(self.project.client, self.client)
        self.assertEqual(self.project.created_at, self.created_at)
        self.assertEqual(self.project.updated_at, self.updated_at)

    def test_read_project(self):
        self.getProject = Project.objects.get(id=self.projectID)
        self.assertEqual(self.getProject.name, "Philip")
        self.assertEqual(self.getProject.state, "New")
        self.assertEqual(self.getProject.client, self.client)
        self.assertEqual(self.getProject.created_at, self.created_at)
        self.assertEqual(self.getProject.updated_at, self.updated_at)

    def test_update_project(self):
        self.getProject = Project.objects.get(id=self.projectID)
        self.getProject.name="Logic Morph"
        self.getProject.save()
        self.updated_at=self.getProject.updated_at

        self.assertEqual(self.getProject.name, "Logic Morph")
        self.assertEqual(self.getProject.state, "New")
        self.assertEqual(self.getProject.client, self.client)
        self.assertEqual(self.getProject.created_at, self.created_at)
        self.assertEqual(self.getProject.updated_at, self.updated_at)


    def test_delete_project(self):
        Project.objects.get(id=self.projectID).delete()
        counts = Project.objects.filter(id=self.projectID).count()
        self.assertEqual(counts, 0)
