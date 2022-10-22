from django.test import TestCase
from datetime import datetime
from app.models import Post
from accounts.models.user import User

class TestPostModels(TestCase):  

    def create_user(self)  :
        self.created_by=User.objects.create(
            username="userJuan",
            password="secretnijuan",
            first_name="Juan",
            last_name="Delacruz",
            email="flipdruid@yahoo.com"
        )
        self.title="Post"
        self.current_date = datetime.strptime(str(datetime.now()), '%Y-%m-%d %H:%M:%S.%f').date()
        return self.created_by

    def create_post(self):

        self.post=Post.objects.create(
            title=self.title,
            description="Post One",
            created_by =self.created_by,
            created_at = datetime.today().strftime('%Y-%m-%d'),
            updated_at= datetime.today().strftime('%Y-%m-%d')  
        )
        self.created_at=self.post.created_at
        self.updated_at=self.post.updated_at
        return self.post

    def setUp(self):      
        self.created_by = self.create_user()  
        self.post=self.create_post()        
    
    def tearDown(self):
        self.post=None
        self.created_by=None

    def test_title_str(self):
        self.assertEqual(str(self.post.title), "Post")
        self.assertEqual(str(self.post.description), "Post One")
        self.assertEqual(self.post.created_by, self.created_by)
        self.assertEqual(self.post.created_at, self.created_at)
        self.assertEqual(self.post.updated_at, self.updated_at)