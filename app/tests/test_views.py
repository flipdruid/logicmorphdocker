# import imp
# from urllib import response
# from django.test import TestCase, Client
# from django.urls import reverse
# from app.models import Lead, Profile, Post, Project
# from django.utils.text import slugify
# import json

# class TestViews(TestCase):

#     def setUP(self):
#         self.client=Client()
#         self.lead_url=reverse('contact_us')

#     def test_lead_list_GET(self):
#         # client = Client()
#         response = self.client.get(reverse('contact_us'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'main/contact_us.html')
        
#     def test_post_list_GET(self):
#         response =  self.client.get(reverse('post'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'main/post_add.html')
        


