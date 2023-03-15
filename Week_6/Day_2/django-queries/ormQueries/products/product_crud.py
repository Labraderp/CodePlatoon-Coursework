from .models import Product
import pprint

pp = pprint.PrettyPrinter(indent=2,depth=2)
class ProductCrud():
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()
    
    def find_by_model(model_to_find):
        return Product.objects.get(model=model_to_find)
    
    def last_record():
        count=0
        for vals in Product.objects.all():
            count += 1
        return Product.objects.get(id=count)
    
    def by_rating(num):
        query_set = Product.objects.all()
        return query_set.filter(rating=num)
    
    def by_rating_range(low, high):
        query_set = Product.objects.all()
        
        query_set = query_set.filter(rating__gte=low)
        query_set = query_set.filter(rating__lte=high)
        return query_set
    
    def by_rating_and_color(num, wanted_color):
        query_set = Product.objects.all()

        query_set = query_set.filter(rating=num)
        query_set = query_set.filter(color=wanted_color)

        return query_set
    
    def by_rating_or_color(num, wanted_color):
        query_set = Product.objects.all()
        query_set = query_set.filter(rating=num) | query_set.filter(color=wanted_color)

        return query_set
    
    def no_color_count():
        count = 0
        for vals in Product.objects.all():
            if vals.color == None:
                count += 1
        return count
    
    def below_price_or_above_rating(price, rating):
        query_set = Product.objects.all()
        query_set = query_set.filter(price_cents__lt=price) | query_set.filter(rating__gt=rating)

        return query_set
    
    def ordered_by_category_alphabetical_order_and_then_price_decending():
        query_set = Product.objects.all()
        return query_set.order_by('category', 'manufacturer', '-price_cents')      