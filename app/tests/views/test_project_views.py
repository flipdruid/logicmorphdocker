from django.urls import reverse_lazy
from django.test import TestCase, Client
from accounts.models.user import User
from django.contrib.auth.models import Group
  
class TestProjectViews(TestCase):  
    def setUp(self):

        self.credentials = {
            'username': 'userJuan',
            'password': 'secretnijuan',
            'first_name':'Juan',
            'last_name' : 'Delacruz',
            'email': 'testemail@email.com',
            'is_active': 'True',
            }
        self.user=User.objects.create(**self.credentials) 
        
        self.client=Client()
        self.CreateProjectClient_url= reverse_lazy("create_client_project")
        self.CreateProject_url= reverse_lazy("create_client_project")
        self.ListProject_url= reverse_lazy("list_project")
        self.ListClientProject_url= reverse_lazy("list_client_project")

        self.postcreate_url= reverse_lazy("post")
        self.login_url= reverse_lazy("accounts:login")
        
    def test_CreateProjectClient(self):
        self.client.login(email=self.user.email, password=self.user.password)
        response = self.client.get(self.CreateProjectClient_url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_CreateProject(self):
        self.client.login(email=self.user.email, password=self.user.password)
        response = self.client.get(self.CreateProject_url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_ListProject(self):
        self.client.login(email=self.user.email, password=self.user.password)
        response = self.client.get(self.ListProject_url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_ListClientProject(self):
        self.client.login(email=self.user.email, password=self.user.password)
        response = self.client.get(self.ListClientProject_url, follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_ClientProjectUpdate(self):
        self.client.login(email=self.user.email, password=self.user.password)
        response = self.client.get('accounts/portal/clientprojectupdate/1/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_ClientProjectDelete(self):
        self.client.login(email=self.user.email, password=self.user.password)
        response = self.client.get('accounts/portal/clientprojectdelete/1/', follow=True)
        self.assertEqual(response.status_code, 200)
    
