# from urllib import response
# from django.urls import reverse_lazy
# from django.test import TestCase, Client
# from accounts.models.user import User

# class TestUserViews(TestCase):

#     def setUp(self):
#         self.credentials = {
#             'username': 'userJuan',
#             'password': 'secretnijuan',
#             'first_name':'Juan',
#             'last_name' : 'Delacruz',
#             'email': 'testemail@email.com',
#             'is_active': 'True'
#             }
#         self.user=User.objects.create(**self.credentials)        

#         self.client=Client()
#         self.index_url= reverse_lazy("accounts:home")
#         self.login_url= reverse_lazy("accounts:login")
#         self.logout_url= reverse_lazy("accounts:logout")
#         self.profile_url= reverse_lazy("accounts:profile")
#         self.register_url= reverse_lazy("accounts:register")
#         self.activate_complete_url= reverse_lazy("accounts:django_registration_activation_complete")
#         self.change_password_url= reverse_lazy("accounts:change_password")
#         self.change_password_done_url= reverse_lazy("accounts:change_password_done")
#         self.reset_password_url= reverse_lazy("accounts:reset_password")
#         self.reset_password_done_url= reverse_lazy("accounts:password_reset_done")
#         self.reset_password_complete_url= reverse_lazy("accounts:password_reset_complete")

#     def test_IndexView(self):        
#         response = self.client.get(self.index_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response,"accounts/home.html")

#     def test_login(self):
#         response = self.client.get(self.login_url,self.credentials, follow=True)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response,"accounts/login.html")   
    
#     def test_logout(self):
#         self.client.login(username=self.user.username, password=self.user.password)
#         response = self.client.get(self.logout_url, follow=True)
#         self.assertEqual(response.status_code, 200)

#     def test_profile(self):
#         self.client.login(username=self.user.username, password=self.user.password)
#         response = self.client.get(self.profile_url, follow=True)
#         self.assertEqual(response.status_code, 200)

#     def test_register(self):
#         response = self.client.get(self.register_url)
#         self.assertEqual(response.status_code, 200)
    
#     def test_activate_user(self):
#         self.client.login(username=self.user.username, password=self.user.password)
#         response = self.client.get("activation/activation_key/", follow=True)
#         self.assertEqual(response.status_code, 200)

#     def test_activate_complete(self):
#         self.client.login(username=self.user.username, password=self.user.password)
#         response = self.client.get(self.activate_complete_url, follow=True)
#         self.assertEqual(response.status_code, 200)

#     def test_change_password(self):
#         self.client.login(username=self.user.username, password=self.user.password)
#         response = self.client.get(self.change_password_url, follow=True)
#         self.assertEqual(response.status_code, 200)

#     def test_change_password_done(self):
#         self.client.login(username=self.user.username, password=self.user.password)
#         response = self.client.get(self.change_password_done_url, follow=True)
#         self.assertEqual(response.status_code, 200)

#     def test_reset_password(self):
#         self.client.login(username=self.user.username, password=self.user.password)
#         response = self.client.get(self.reset_password_url, follow=True)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response,"accounts/password_reset_form.html")

#     def test_reset_password_done(self):
#         self.client.login(username=self.user.username, password=self.user.password)
#         response = self.client.get(self.reset_password_done_url, follow=True)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response,"accounts/password_reset_done.html")

#     def test_reset_password_confirm(self):
#         self.client.login(username=self.user.username, password=self.user.password)
#         response = self.client.get("/accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$", follow=True)
#         self.assertEqual(response.status_code, 200)
    
#     def test_reset_password_complete(self):
#         self.client.login(username=self.user.username, password=self.user.password)
#         response = self.client.get(self.reset_password_complete_url, follow=True)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response,"accounts/password_reset_complete.html")