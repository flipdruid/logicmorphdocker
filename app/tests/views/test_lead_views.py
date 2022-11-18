from django.urls import reverse_lazy
from django.test import TestCase, Client
from accounts.models.user import User
  
class TestLeadViews(TestCase):  

    def setUp(self):

        self.credentials = {
            'username': 'userJuan',
            'password': 'secretnijuan',
            'first_name':'Juan',
            'last_name' : 'Delacruz',
            'email': 'testemail@email.com',
            'is_active': 'True'
            }
        self.user=User.objects.create(**self.credentials)         
        self.client=Client()

        self.LeadCreate_url= reverse_lazy("contact_us")
        self.LeadMailList_url= reverse_lazy("lead_mail_lists")
        self.leadactivation_url= reverse_lazy("user_profile")
        
    def test_LeadCreate(self):
        self.client.login(username=self.user.username, password=self.user.password)
        response = self.client.get(self.LeadCreate_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"main/contact_us_mail.html")

    def test_LeadMailList(self):
        self.client.login(username=self.user.username, password=self.user.password)
        response = self.client.get(self.LeadMailList_url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_LeadMailView(self):
        self.client.login(username=self.user.username, password=self.user.password)
        response = self.client.get("portal/mailview/1/", follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_LeadMailDelete(self):
        self.client.login(username=self.user.username, password=self.user.password)
        response = self.client.get("portal/mailviewlead/1/", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_LeadToClient(self):
        self.client.login(username=self.user.username, password=self.user.password)
        response = self.client.get("portal/leadclient/1/", follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_createreglink(self):
        self.client.login(username=self.user.username, password=self.user.password)
        response = self.client.get("portal/createreglink/1/", follow=True)
        self.assertEqual(response.status_code, 200)

    
    def test_leadactivation(self):
        self.client.login(username=self.user.username, password=self.user.password)
        response = self.client.get("portal/leadactivation/1/", follow=True)
        self.assertEqual(response.status_code, 200)
        
    def test_leadactivation(self):
        self.client.login(username=self.user.username, password=self.user.password)
        response = self.client.get(self.leadactivation_url, follow=True)
        self.assertEqual(response.status_code, 200)