from django.test import TestCase
from .models import *
import redgreenunittest as unittest

class AssociationTestCase(TestCase):
    def setUp(self):
        self.shop_owner = User.objects.create()
        self.shop = Shop.objects.create(owner=self.shop_owner)
        self.product = Product.objects.create(shop=self.shop)
        self.user = User.objects.create()
        self.review = Review.objects.create(product=self.product, user=self.user)

    def test_01_owner_of_shop(self):
        """returns the owner of the shop"""
        self.assertEqual(self.shop.owner, self.shop_owner)

    def test_02_shop_products(self):
        """returns the products for sale in the shop"""
        self.assertEqual(list(self.shop.products.all()), [self.product])

    def test_03_product_shop(self):
        """returns the shop the product belongs to"""
        self.assertEqual(self.product.shop, self.shop)

    def test_04_product_reviews(self):
        """returns the product's reviews"""
        self.assertEqual(list(self.product.reviews.all()), [self.review])

    def test_05_review_reviewer(self):
        """returns the review's author"""
        self.assertEqual(self.review.user, self.user)
