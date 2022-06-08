from django.test import TestCase
from accounts.models import Profile
from django.contrib.auth.models import User


class TestProfile(TestCase):
    """Test case for Profile model"""

    def setUp(self):
        """Set up for the models instances"""
        self.user = User.objects.create(
            username='Doe', email="doe@gmail.com", password="pass11234")
        self.user2 = User.objects.create(
            username='Jane', email='jane@gmail.com', password='pass11234')
        self.profile = self.user.profile
        self.profile2 = self.user2.profile

    def tearDown(self):
        """Method to clear the model objects in the db after each testcase"""
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_profile_instance(self):
        """Test case to check if created profile is instance of Profile model class"""
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertTrue(isinstance(self.profile2, Profile))

    def test_follow_user(self):
        """Test case to check if a user can follow another user and the added to the list of followers"""
        self.profile.followers.add(self.user2)
        self.profile2.following.add(self.user)
        self.assertEqual(len(self.profile.followers.all()), 1)
        self.assertEqual(len(self.profile2.following.all()), 1)

    def test_unfollow_user(self):
        """Test case to check if a user can unfollow another user and the removed to the list of followers"""
        self.profile.followers.add(self.user2)
        self.profile2.following.add(self.user)
        self.profile.followers.remove(self.user2)
        self.profile2.following.remove(self.user)
        self.assertEqual(len(self.profile.followers.all()), 0)
        self.assertEqual(len(self.profile2.following.all()), 0)
