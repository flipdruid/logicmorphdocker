from django.urls import reverse_lazy
from django.test import TestCase, Client

  
class TestIndexViews(TestCase):

    def setUp(self):        
        self.client=Client()
        self.landing_url= reverse_lazy("main")
        
    def test_landing(self):
        response = self.client.get(self.landing_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"main/landing.html")