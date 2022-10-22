from django.urls import reverse_lazy
from django.test import TestCase, Client
  
class TestLeadViews(TestCase):  

    def setUp(self):
        self.leadcreate_url= reverse_lazy("contact_us")
        
    def test_lead_create(self):
        response = self.client.get(self.leadcreate_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"main/contact_us.html")