from django.test import TestCase
from datetime import datetime
from app.models import Post
from accounts.models.user import User

class TestPostModels(TestCase):    

    def setUp(self):        

        self.created_by=User.objects.create(
            username="userJuan",
            password="secretnijuan",
            first_name="Juan",
            last_name="Delacruz",
            email="flipdruid@yahoo.com"
        )

        self.title="Post"
        self.current_date = datetime.strptime(str(datetime.now()), '%Y-%m-%d %H:%M:%S.%f').date()
        self.post=Post.objects.create(
            title=self.title,
            description="Post One",
            created_by =self.created_by,
            created_at = datetime.today().strftime('%Y-%m-%d'),
            updated_at= datetime.today().strftime('%Y-%m-%d')          

        )    
    def test_title_str(self):
        self.assertEqual(str(self.post.title), "Post")
            
    def test_description_str(self):
        self.assertEqual(str(self.post.description), "Post One")
    
    def test_created_at_str(self):
        self.expected_date = self.post.created_at
        self.assertEqual(str(self.post.created_at), str(self.expected_date))
    
    def test_updated_at_str(self):
        self.expected_date = self.post.updated_at
        self.assertEqual(str(self.post.updated_at), str(self.expected_date))

    def test_username_str(self):
        self.username = "userJuan"
        self.assertEqual(str(self.username), str(self.created_by.username))
    
    def test_password_str(self):
        self.password = "secretnijuan"
        self.assertEqual(str(self.password), str(self.created_by.password))

    def test_first_name_str(self):
        self.first_name = "Juan"
        self.assertEqual(str(self.first_name), str(self.created_by.first_name))

    def test_last_name_str(self):
        self.last_name = "Delacruz"
        self.assertEqual(str(self.last_name), str(self.created_by.last_name))
    
    def test_email_str(self):
        self.email = "flipdruid@yahoo.com"
        self.assertEqual(str(self.email), str(self.created_by.email))

    def test_created_by_str(self):
        expected_creator = self.created_by
        self.assertEqual(str(expected_creator), str(self.post.created_by))
            