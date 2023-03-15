from django.test import TestCase
from .models import *
import redgreenunittest as unittest

class AssociationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create()
        self.restaurant = Restaurant.objects.create()
        self.order = Order.objects.create(user=self.user, restaurant=self.restaurant)
        self.food_item_1 = FoodItem.objects.create()
        self.food_item_2 = FoodItem.objects.create()
        self.food_item_3 = FoodItem.objects.create()
        self.food_item_4 = FoodItem.objects.create()
        self.order_food_item_1 = OrderFoodItem.objects.create(order=self.order, food_item=self.food_item_1)
        self.order_food_item_2 = OrderFoodItem.objects.create(order=self.order, food_item=self.food_item_2)
        self.order_food_item_3 = OrderFoodItem.objects.create(order=self.order, food_item=self.food_item_3)
        self.order_food_item_4 = OrderFoodItem.objects.create(order=self.order, food_item=self.food_item_4)

    def test_01_user_orders(self):
        """returns the user's orders"""
        self.assertEqual(list(self.user.orders.all()),[self.order])

    def test_02_orders_user(self):
        """returns the order's user"""
        self.assertEqual(self.order.user, self.user)

    def test_03_restaurant_orders(self):
        """returns the restauants orders"""
        self.assertEqual(list(self.restaurant.orders.all()), [self.order])

    def test_04_order_restaurant(self):
        """returns the order's restaurant"""
        self.assertEqual(self.order.restaurant, self.restaurant)

    def test_05_orders_food_items(self):
        """returns the order's food items"""
        self.assertEqual(list(self.order.food_items.all()), [self.food_item_1, self.food_item_2, self.food_item_3, self.food_item_4])

    def test_06_food_item_orders(self):
        """returns all orders that contain the food item"""
        self.assertEqual(list(self.food_item_1.orders.all()), [self.order])
        self.assertEqual(list(self.food_item_2.orders.all()), [self.order])
        self.assertEqual(list(self.food_item_3.orders.all()), [self.order])
        self.assertEqual(list(self.food_item_4.orders.all()), [self.order])

    def test_07_users_food_items(self):
        """returns all the food items in the order"""
        all_food_items = list(list((order.food_items.all()) for order in list(self.user.orders.all()))[0])
        self.assertEqual(all_food_items, [self.food_item_1, self.food_item_2, self.food_item_3, self.food_item_4])
