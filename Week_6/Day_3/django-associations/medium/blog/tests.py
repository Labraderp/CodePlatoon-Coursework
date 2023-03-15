from django.test import TestCase
from .models import *

class AssociationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create()
        self.post = Post.objects.create(author=self.user)
        self.commenter_one = User.objects.create()
        self.commenter_two = User.objects.create()
        self.comment_one = Comment.objects.create(post=self.post, author=self.commenter_one)
        self.comment_two = Comment.objects.create(post=self.post, author=self.commenter_two)

    def test_01_author_of_post(self):
        """returns the author of the post"""
        self.assertEqual(self.post.author, self.user)

    def test_02_posts_comments(self):
        """returns the post's comments"""
        self.assertEqual(list(self.post.comments.all()), [self.comment_one, self.comment_two])

    def test_03_comments_author(self):
        """returns the comment's author(user)"""
        self.assertEqual(self.comment_one.author, self.commenter_one)

    def test_04_comments_post(self):
        """returns the comment's post"""
        self.assertEqual(self.comment_two.post, self.post)

    def test_05_users_posts(self):
        """returns the posts written by this user"""
        self.assertEqual(list(self.user.posts.all()), [self.post])

    def test_06_users_comments(self):
        """returns the comments created by the user"""
        self.assertEqual(list(self.commenter_two.comments.all()), [self.comment_two])
