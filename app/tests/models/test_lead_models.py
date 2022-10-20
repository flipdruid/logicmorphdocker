from tarfile import CONTTYPE
from django.test import TestCase
from datetime import datetime, date
from app.models import Lead
  
currentTime = datetime.now()
# dates=datetime.strptime(str(currentTime), '%Y-%m-%d')
dates = currentTime.strftime('%Y-%m-%d')
class TestLeadModels(TestCase):
    
    def setUp(self):
        self.lead=Lead.objects.create(
            first_name="Verlien",
            last_name="Lebios",
            email="flipdruid@yahoo.com",
            entity_name="Subject",
            details="details",
            created_at= dates,
            updated_at= dates
        ) 
        

    def test_first_name_str(self):
        self.first_name="Verlien"
        self.assertEqual(self.first_name, self.lead.first_name)
            
    def test_last_name_str(self):
        self.last_name="Lebios"
        self.assertEqual(self.last_name, self.lead.last_name)

    def test_email_str(self):
        self.email="flipdruid@yahoo.com"
        self.assertEqual(self.email, self.lead.email)
        
    def test_entity_name_str(self):
        self.entity_name="Subject"
        self.assertEqual(self.entity_name, self.lead.entity_name)
    
    def test_details_str(self):
        self.details="details"
        self.assertEqual(self.details, self.lead.details)

    def test_created_at_str(self):
        self.assertEqual(str(self.lead.created_at), str(self.lead.created_at))

    def test_updated_at_str(self):
        self.assertEqual(str(self.lead.updated_at), str(self.lead.updated_at))
