from tarfile import CONTTYPE
from unicodedata import name
from django.test import TestCase
from datetime import datetime
from app.models.client import Client
from app.models.project import Project
  
currentTime = datetime.now()
# dates=datetime.strptime(str(currentTime), '%Y-%m-%d')
dates = currentTime.strftime('%Y-%m-%d')
class TestClientModels(TestCase):
    
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
    

    def test_name_str(self):
        self.assertEqual(self.project.name, "Philip")
    
    def test_state_str(self):
        self.assertEqual(self.project.state, "New")

    def test_client_object(self):
        self.assertEqual(self.project.client, self.client)

    def test_created_at_str(self):
        self.expected_date = self.project.created_at
        self.assertEqual(str(self.project.created_at), str(self.expected_date))
    
    def test_updated_at_str(self):
        self.expected_date = self.project.updated_at
        self.assertEqual(str(self.project.updated_at), str(self.expected_date))