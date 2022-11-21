from django.test import TestCase
from datetime import date
from app.models.client import Client
from app.models.profile import Profile
from accounts.models.user import User

  
class TestLeadModels(TestCase):  
    def create_client(self):

        self.credentials = {
            'username': 'userJuan',
            'password': 'secretnijuan',
            'first_name':'Juan',
            'last_name' : 'Delacruz',
            'email': 'testemail@email.com',
            'is_active': 'True'
            }

        self.user = User.objects.create(**self.credentials)

        self.profile = Profile.objects.create(
            user = self.user,
            avatar = 'avatar.jpg',
            is_logicmorph_staff = False,
            is_dark_theme = False
        )

        self.client=Client.objects.create(
            business_name='Logic Morph',
            business_logo="logo.png",
            address="Philippines",
            telephone_no="123456",
            position ="Developer",
            profile = self.profile
        )   
        return self.client

    def setUp(self):
        self.client=self.create_client()

    def tearDown(self):
        self.client=None

    def test_create_client(self):
        self.assertEqual(str(self.client.business_name), 'Logic Morph')
        self.assertEqual(str(self.client.business_logo), "logo.png")
        self.assertEqual(str(self.client.address), "Philippines")
        self.assertEqual(str(self.client.telephone_no), "123456")
        self.assertEqual(str(self.client.position), "Developer")
        self.assertEqual(self.client.profile, self.profile)

    def test_read_client(self):
        self.getClient = Client.objects.get(profile=self.profile)
        self.assertEqual(str(self.client.business_name), 'Logic Morph')
        self.assertEqual(str(self.client.business_logo), "logo.png")
        self.assertEqual(str(self.client.address), "Philippines")
        self.assertEqual(str(self.client.telephone_no), "123456")
        self.assertEqual(str(self.client.position), "Developer")
        self.assertEqual(self.client.profile, self.profile)

    def test_update_client(self):
        self.getClient = Client.objects.get(profile=self.profile)
        self.getClient.business_name = 'Logic Morph 2'
        self.getClient.business_logo='logo2.png'
        self.getClient.address='Philippines 2'
        self.getClient.telephone_no='789'
        self.getClient.position='Developer 2'
        self.getClient.save()

        self.assertEqual(str(self.getClient.business_name), 'Logic Morph 2')
        self.assertEqual(str(self.getClient.business_logo), "logo2.png")
        self.assertEqual(str(self.getClient.address), "Philippines 2")
        self.assertEqual(str(self.getClient.telephone_no), "789")
        self.assertEqual(str(self.getClient.position), "Developer 2")
        self.assertEqual(self.getClient.profile, self.profile)

    def test_delete_client(self):
        Client.objects.get(profile=self.profile).delete()
        counts = Client.objects.filter(profile=self.profile).count()
        self.assertEqual(counts, 0)