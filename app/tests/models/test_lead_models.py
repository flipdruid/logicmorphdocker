from tarfile import CONTTYPE
from django.test import TestCase
from datetime import datetime
from app.models import Lead


class TestLeadModels(TestCase):

    def create_lead(self):
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
        self.leadID = self.lead.id
        return self.lead

    
    def setUp(self):
        self.lead=self.create_lead()

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

    
    def test_read_lead(self):
        self.getLead = Lead.objects.get(id=self.leadID)
        self.assertEqual(self.getLead.first_name, "Verlien")
        self.assertEqual(self.getLead.last_name,"Lebios")
        self.assertEqual(self.getLead.email, "flipdruid@yahoo.com")
        self.assertEqual(self.getLead.entity_name, "Subject")
        self.assertEqual(self.getLead.details, "details")
        self.assertEqual(str(self.created_at), str(self.lead.created_at))
        self.assertEqual(str(self.updated_at), str(self.lead.updated_at))

    
    def test_update_lead(self):
        self.getLead = Lead.objects.get(id=self.leadID)
        self.getLead.first_name="Berlito"
        self.getLead.last_name = "Artus"
        self.getLead.entity_name="New Subject"
        self.getLead.details="New Details"
        self.getLead.save()
        self.updated_at = self.getLead.updated_at

        self.assertEqual(self.getLead.first_name, "Berlito")
        self.assertEqual(self.getLead.last_name,"Artus")
        self.assertEqual(self.getLead.email, "flipdruid@yahoo.com")
        self.assertEqual(self.getLead.entity_name, "New Subject")
        self.assertEqual(self.getLead.details, "New Details")
        self.assertEqual(str(self.created_at), str(self.getLead.created_at))
        self.assertEqual(str(self.updated_at), str(self.getLead.updated_at))


    def test_delete_lead(self):
        Lead.objects.get(id=self.leadID).delete()
        counts = Lead.objects.filter(id=self.leadID).count()
        self.assertEqual(counts, 0)