from django.test import TestCase
from .models import *
import redgreenunittest as unittest

class AssociationTestCase(TestCase):
    def setUp(self):
        self.actor = Actor()
        self.actor.save()
        self.movie = Movie()
        self.movie.save()
        self.role  = Role(movie=self.movie, actor=self.actor)
        self.role.save()

    def test_01_roles_movie(self):
        """returns the role's movie"""
        self.assertEqual(self.role.movie, self.movie)

    def test_02_roles_actor(self):
        """returns the role's actor"""
        self.assertEqual(self.role.actor, self.actor)

    def test_03_movies_roles(self):
        """returns the movie's roles"""
        self.assertEqual(list(self.movie.roles.all()), [self.role])

    def test_04_movies_actors(self):
        """returns the movie's actors"""
        self.assertEqual(list(self.movie.actors.all()), [self.actor])

    def test_05_actors_roles(self):
        """returns the actor's roles"""
        self.assertEqual(list(self.actor.roles.all()), [self.role] )

    def test_06_actors_movies(self):
        """returns the actor's movies"""
        self.assertEqual(list(self.actor.movies.all()), [self.movie])
