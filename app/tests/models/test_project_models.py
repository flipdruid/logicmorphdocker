from tarfile import CONTTYPE
from unicodedata import name
from django.test import TestCase
from datetime import datetime
from app.models.client import Client
from app.models.project import Project

class TestProjectModels(TestCase):
    
    def setUp(self):
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
        self.created_at=self.project.created_at
        self.updated_at=self.project.updated_at
    
    def tearDown(self):
        self.client=None
        self.project=None
        
    def test_create_project_str(self):
        self.assertEqual(self.project.name, "Philip")
        self.assertEqual(self.project.state, "New")
        self.assertEqual(self.project.client, self.client)
        self.assertEqual(self.project.created_at, self.created_at)
        self.assertEqual(self.project.updated_at, self.updated_at)