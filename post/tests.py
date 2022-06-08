from django.test import TestCase
from accounts.models import Profile
from django.contrib.auth.models import User
from post.models import Post, Comment


class TestProfile(TestCase):
    """Test case for Post model"""

    def setUp(self):
        """Set up for the models instances"""
        self.user = User.objects.create(
            username='Doe', email="doe@gmail.com", password="pass11234")
        self.user2 = User.objects.create(
            username='Jane', email='jane@gmail.com', password='pass11234')
        self.profile = self.user.profile
        self.profile2 = self.user2.profile
        self.post = Post.objects.create(
            poster=self.profile, image='image.png', captions="Post captions")

    def tearDown(self):
        """Method to clear the model objects in the db after each testcase"""
        User.objects.all().delete()
        Profile.objects.all().delete()
        Post.objects.all().delete()

    def test_post_instance(self):
        """Test case to check if created post is instance of Post model class"""
        self.assertTrue(isinstance(self.post, Post))

    def test_add_comment(self):
        """Test case to check if a user can comment on a post and the comment added to the list of comment"""
        self.comment = Comment.objects.create(
            user=self.user, comment="Test comment", post=self.post)
        self.post.comments.add(self.comment)
        self.assertTrue(isinstance(self.comment, Comment))
        self.assertEqual(len(self.post.comments.all()), 1)

    def test_add_like(self):
        """Test case to add a like to a post and the user is added to the list of likes"""
        self.post.likes.add(self.user2)
        self.assertEqual(len(self.post.likes.all()), 1)

    def test_remove_like(self):
        """Test remove a like (user) from the list of likes"""
        self.post.likes.add(self.user2)
        self.post.likes.remove(self.user2)
        self.assertEqual(len(self.post.likes.all()), 0)


class TestComment(TestCase):
    """Test class for Comment model"""

    def setUp(self):
        """Set up for the models instances"""

        self.user = User.objects.create(
            username='Doe', email="doe@gmail.com", password="pass11234")
        self.profile = self.user.profile
        self.post = Post.objects.create(
            poster=self.profile, image='image.png', captions="Post captions")
        self.comment = Comment.objects.create(
            user=self.user, comment="Test comment", post=self.post)

    def tearDown(self):
        """Method to clear the model objects in the db after each testcase"""
        User.objects.all().delete()
        Profile.objects.all().delete()
        Post.objects.all().delete()
        Comment.objects.all().delete()

    def test_comment_instance(self):
        """Test case to check if created comment is instance of Comment model class"""
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        """Test save comment to check if created comment exists in the database"""
        comments = Comment.objects.all()
        self.assertEqual(len(comments), 1)
