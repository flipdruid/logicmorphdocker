# from sqlite3 import Timestamp
# from accounts.models.user import User
# from datetime import datetime
# from accounts.models.profile import Profile
# from django.test import TestCase

# currentTime = datetime.now()
# dates = currentTime.strftime('%Y-%m-%d')
# class TestProfile(TestCase):

#     def setUp(self):
#         self.user=User.objects.create(
#             username="userJuan",
#             password="secretnijuan",
#             first_name="Juan",
#             last_name="Delacruz",
#             email="flipdruid@yahoo.com"
#         )
#         # user = User(username='user1')
#         self.profile=Profile.objects.create(
#             user=self.user,
#             timestamp=dates
#     #     )
    
#     # def test_profile_user_str(self):
#     #     expected_user_info="UserJuan"
#     #     self.assertEqual(str(expected_user_info), str(self.profile.user.username))

#     def test_timestamp_str(self):
#         self.timestamp  = self.profile.timestamp
#         self.assertEqual(str(self.timestamp), str(self.profile.timestamp))