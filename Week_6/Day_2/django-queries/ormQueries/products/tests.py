from django.test import TestCase
from .models import Product
from .product_crud import ProductCrud

def get_query_ids(queryset):
    return list(queryset.values_list('id', flat=True))

class ProductCrudTestCase(TestCase):
    fixtures = ['products.yaml']

    def test_01_get_all_products(self):
        """Returns all Products"""
        product_crud = ProductCrud.get_all_products()
        product = Product.objects.all()
        self.assertEqual(list(product_crud), list(product))

    def test_02_find_by_model(self):
        """finds the matching product by model name"""
        product_crud = ProductCrud.find_by_model("Heavy Duty Steel Clock")
        product = Product.objects.get(id=3)
        self.assertEqual(product_crud, product)

    def test_03_last_record(self):
        """finds the last record inserted"""
        product_crud = ProductCrud.last_record()
        product = Product.objects.get(id=30)
        self.assertEqual(product_crud, product)

    def test_04_by_rating(self):
        """finds products by their rating"""
        product_crud = ProductCrud.by_rating(3.5)
        product_ids = get_query_ids(product_crud)
        self.assertEquals(product_ids, [7, 8, 9, 20, 24])

    def test_05_by_rating_range(self):
        """finds products within a rating range"""
        product_crud = ProductCrud.by_rating_range(1.1, 1.5)
        product_ids = get_query_ids(product_crud)
        self.assertEquals(product_ids, [14, 15, 16, 18, 21])

    def test_06_by_rating_and_color(self):
        """finds products by rating & color value"""
        product_crud = ProductCrud.by_rating_and_color(3.5, 'maroon')
        product_ids = get_query_ids(product_crud)
        self.assertEquals(product_ids, [7])

    def test_07_by_rating_or_color(self):
        """finds products by a rating or color value"""
        product_crud = ProductCrud.by_rating_or_color(4.3 , 'blue')
        product_ids = get_query_ids(product_crud)
        self.assertEquals(product_ids, [5, 15])

    def test_08_no_color_count(self):
        """returns the count of products that have no color value"""
        self.assertEquals(ProductCrud.no_color_count(), 22)

    def test_09_below_price_or_above_rating(self):
        """returns products below a price or above a rating"""
        product_crud = ProductCrud.below_price_or_above_rating(1000, 4.0)
        product_ids = get_query_ids(product_crud)
        self.assertEquals(product_ids, [2, 3, 4, 5, 11, 22, 25])

    def test_10_ordered_by_category_alphabetical_order_and_then_price_decending(self):
        """returns products ordered by category alphabetical and decending price"""
        product_crud = ProductCrud.ordered_by_category_alphabetical_order_and_then_price_decending()
        product_ids = get_query_ids(product_crud)
        self.assertEquals(product_ids, [1, 18, 10, 27, 29, 21, 9, 7, 15, 5, 19, 8, 4, 30, 14, 22, 16, 13, 26, 3, 28, 23, 24, 25, 17, 12, 2, 20, 11, 6])

    def test_11_products_by_manufacturer(self):
        """returns products made by manufacturers with names containing an input string"""
        product_crud = ProductCrud.products_by_manufacturer_with_name_like('Group')
        product_ids = get_query_ids(product_crud)
        self.assertEquals(product_ids, [2, 3, 6, 29])

    def test_12_manufacturer_names_for_query(self):
        """returns a list of manufacturer names that match query"""
        product_crud = ProductCrud.manufacturer_names_for_query('Group')
        self.assertCountEqual(product_crud, ["Lakin Group", "Nikolaus Group","Rolfson Group", "Watsica Group"])

    def test_13_not_in_a_category(self):
        """returns products that are not in a category"""
        product_crud = ProductCrud.not_in_a_category('Garden')
        product_ids = get_query_ids(product_crud)
        self.assertEquals(product_ids, list(range(1,30)))

    def test_14_limited_not_in_a_category(self):
        """returns products that are not in a category up to a limit"""
        product_crud = ProductCrud.limited_not_in_a_category('Garden', 3)
        product_ids = get_query_ids(product_crud)
        self.assertEquals(product_ids, [1, 2, 3 ])

    def test_15_category_manufacturers(self):
        """returns an array of manufacturers for a category"""
        product_crud = ProductCrud.category_manufacturers('Baby')
        self.assertCountEqual(product_crud,["Cormier, Rice and Ledner", "Crooks, Pacocha and Rohan","Howell, Hills and Dickens", "Muller-Koss", "Rolfson Group"])

    def test_16_average_category_rating(self):
        """returns the average"""
        product_crud = ProductCrud.average_category_rating('Baby')
        self.assertEqual(product_crud['rating__avg'], 2.32)

    def test_17_greatest_price(self):
        """returns the highest price"""
        product_crud = ProductCrud.greatest_price()
        self.assertEquals(product_crud['price_cents__max'], 9758)

    def test_18_longest_model_name(self):
        """returns the id of the product with the longest model name"""
        product_crud = ProductCrud.longest_model_name()
        self.assertEquals(product_crud, 25)

    def test_19_ordered_by_model_length(self):
        """returns products ordered by the length of their model name"""
        product_crud = ProductCrud.ordered_by_model_length()
        product_ids = get_query_ids(product_crud)
        self.assertEquals(product_ids, [8, 28, 15, 11, 27, 5, 17, 10, 7, 1, 9, 12, 26, 30, 2, 13, 3, 4, 21, 24, 29, 16, 14, 20, 23, 18, 6, 22, 19, 25])
