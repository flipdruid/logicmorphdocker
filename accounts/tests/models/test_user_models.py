from accounts.models.user import User
from django.test import TestCase, Client

class TestUser(TestCase):
    def setUp(self):
        self.user=User.objects.create(
            username="userJuan",
            password="secretnijuan",
            first_name="Juan",
            last_name="Delacruz",
            email="flipdruid@yahoo.com"
        )
        client=Client()
        self.userIDD=self.user.id
    def tearDown(self):
        self.user=None
        
    def test_create_user(self):
        self.assertEqual(str(self.user.username), "userJuan" )
        self.assertEqual(str(self.user.password), "secretnijuan") 
        self.assertEqual(str(self.user.first_name), "Juan") 
        self.assertEqual(str(self.user.last_name), "Delacruz")
        self.assertEqual(str(self.user.email), "flipdruid@yahoo.com")

    def test_read_user(self):
        self.getUser = User.objects.get(username='userJuan')
        self.assertEqual(str(self.getUser.username), "userJuan" )
        self.assertEqual(str(self.getUser.password), "secretnijuan") 
        self.assertEqual(str(self.getUser.first_name), "Juan") 
        self.assertEqual(str(self.getUser.last_name), "Delacruz")
        self.assertEqual(str(self.getUser.email), "flipdruid@yahoo.com")

    def test_update_user(self):
        self.getUser = User.objects.get(id=self.userIDD)
        self.getUser.first_name='Juan2'
        self.getUser.last_name='Delacruz2'
        self.getUser.save()

        self.assertEqual(str(self.getUser.username), "userJuan" )
        self.assertEqual(str(self.getUser.password), "secretnijuan") 
        self.assertEqual(str(self.getUser.first_name), "Juan2") 
        self.assertEqual(str(self.getUser.last_name), "Delacruz2")
        self.assertEqual(str(self.getUser.email), "flipdruid@yahoo.com")

    def test_delete_user(self):
        User.objects.get(id=self.userIDD).delete()
        userCount = User.objects.filter(id=self.userIDD).count()
        self.assertEqual(userCount, 0)