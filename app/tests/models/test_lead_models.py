from tarfile import CONTTYPE
from django.test import TestCase
from datetime import datetime
from app.models import Lead
class TestLeadModels(TestCase):
    
    def setUp(self):
        self.lead=Lead.objects.create(
            first_name="Verlien",
            last_name="Lebios",
            email="flipdruid@yahoo.com",
            entity_name="Subject",
            details="details",
            created_at= datetime.today().strftime('%Y-%m-%d'),
            updated_at= datetime.today().strftime('%Y-%m-%d')
        ) 
        
        self.created_at=self.lead.created_at
        self.updated_at=self.lead.updated_at

    def tearDown(self):
        self.lead=None

    def test_create_lead(self):
        self.assertEqual(self.lead.first_name, "Verlien")
        self.assertEqual(self.lead.last_name,"Lebios")
        self.assertEqual(self.lead.email, "flipdruid@yahoo.com")
        self.assertEqual(self.lead.entity_name, "Subject")
        self.assertEqual(self.lead.details, "details")
        self.assertEqual(str(self.created_at), str(self.lead.created_at))
        self.assertEqual(str(self.updated_at), str(self.lead.updated_at))
