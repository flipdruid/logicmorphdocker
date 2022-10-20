from django.test import TestCase
from datetime import date
from app.models import Client
  
class TestLeadModels(TestCase):          
    def setUp(self):
        self.lead=Client.objects.create(
            business_name='Logic Morph',
            business_logo="logo.png",
            address="Philippines",
            telephone_no="123456",
            position ="Developer"
        )    
    def test_business_name_str(self):
        self.assertEqual(str(self.lead.business_name), "Logic Morph")
            
    def test_business_logo_str(self):
        self.assertEqual(str(self.lead.business_logo), "logo.png")

    def test_address_str(self):
        self.assertEqual(str(self.lead.address), "Philippines")
        
    def test_telephone_no_str(self):
        self.assertEqual(str(self.lead.telephone_no), "123456")
    
    def test_position_str(self):
        self.assertEqual(str(self.lead.position), "Developer")
