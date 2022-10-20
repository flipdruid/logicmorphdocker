from django.test import TestCase
from app.models.developer import Developer
from app.models.profile import Profile
from app.models.project import Project
  
class TestLeadModels(TestCase):
    # currentTime = datetime.now().date
    def setUp(self):
        self.developer=Developer.objects.create(
            profile="Verlien",
            role="Dev",
            state="New"
        )    
    def test_profile_str(self):
        self.assertEqual(str(self.developer.profile), "Verlien")
            
    def test_role_str(self):
        self.assertEqual(str(self.developer.role), "Dev")

    def test_state_str(self):
        self.assertEqual(str(self.developer.state), "New")