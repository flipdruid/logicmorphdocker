from django.test import TestCase
from datetime import date
from app.models import Client
  
class TestLeadModels(TestCase):          
    def setUp(self):

        self.client=Client.objects.create(
            business_name='Logic Morph',
            business_logo="logo.png",
            address="Philippines",
            telephone_no="123456",
            position ="Developer"
        )    

    def tearDown(self):
        self.client=None

    def test_create_client(self):
        self.assertEqual(str(self.client.business_name), "Logic Morph")
        self.assertEqual(str(self.client.business_logo), "logo.png")
        self.assertEqual(str(self.client.address), "Philippines")
        self.assertEqual(str(self.client.telephone_no), "123456")
        self.assertEqual(str(self.client.position), "Developer")
