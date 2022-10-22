from django.urls import reverse_lazy
from django.test import TestCase, Client
from accounts.models.user import User
  
class TestPostViews(TestCase):  
    def setUp(self):

        self.credentials = {
            'username': 'userJuan',
            'password': 'secretnijuan',
            'first_name':'Juan',
            'last_name' : 'Delacruz',
            'email': 'testemail@email.com',
            'is_active': 'True'
            }
            
        User.objects.create_user(**self.credentials)
        
        self.client=Client()
        self.landing_url= reverse_lazy("main")
        self.leadcreate_url= reverse_lazy("contact_us")
        self.postcreate_url= reverse_lazy("post")
        self.login_url= reverse_lazy("accounts:login")
        
    def test_lead_create(self):
        response = self.client.get(self.leadcreate_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"main/contact_us.html")

    def test_post_create(self):
        # self.client.login(email=self.credentials['email'], password=self.credentials['password']) // this one works too
        self.client.login(username=self.credentials['username'], password=self.credentials['password'])
        response = self.client.get(self.postcreate_url, follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_post_view(self):
        self.client.login(username=self.credentials['username'], password=self.credentials['password'])
        response = self.client.get('accounts/postview/1', follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_post_edit(self):
        self.client.login(username=self.credentials['username'], password=self.credentials['password'])
        response = self.client.get('accounts/postedit/1', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_post_delete(self):
        self.client.login(username=self.credentials['username'], password=self.credentials['password'])
        response = self.client.get('accounts/postdelete/1', follow=True)
        self.assertEqual(response.status_code, 200)


