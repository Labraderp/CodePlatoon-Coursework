# Django Associations
Now that you have some familiarity with reading and validating records from the database it's time to explore **associations**. 

In this challenge you'll be using the following Django associations:

* ForeignKey (for one to many / many to one associations)
* ManyToManyField (for many to many associations)
* ManyToManyField with through (for adding additional fields to a join table)

## Model Attributes
This challenge is focused on modeling the relationships between models, not the models themselves. For that reason, our tables will not have any columns except for associations. For example an `Actor` model would likely have `first_name` and `last_name` columns as part of the `actors` table, but in this challenge you only need create the necessary `id` & foreign key associations.


## Release 0: IMDB Example
You will create simple schema for the website [IMDB](http://imdb.com) which catalogs movies and actors. Inside the `imdb` folder, you have `imdb` as a project and `moviedb` is the app.

This schema should account for three models:
* Actor
* Role
* Movie

The models can be found in `moviedb/models.py`

The `Role` model joins `Movie` and `Actor.` Via this join model, a movie has many actors and an actor can act in many movies.

Create a virtual environment using the instructions from previous challenges at `django_associations`, install Django, and then run `createdb imdb` to create the database.

Then, set up your models with the appropriate associations. Use the [django documentation](https://docs.djangoproject.com/en/2.1/topics/db/examples/) to help you out. It is important to get comfortable reading through documentation.

After you set up your models run `python manage.py makemigrations <appname>` and then `python manage.py migrate`. If you make alterations to your models you may have to rerun these two commands to update your database and get the tests to pass. If your migrations get too conflicted and broken, you can start over by deleting your migrations folder.

After you set up your models, you can run `python manage.py test`. If you get any error messages, let them guide you toward a solution. 


## Release 1: Medium
Run `createdb medium`. After you set up your models run `python3 manage.py makemigrations <appname>` and then `python3 manage.py migrate`. If you make alterations to your models you may have to rerun these two commands to update your database and get the tests to pass. 

### Models
* Post
* User
* Comment

### Association Methods
```ruby
post.user # the author of the post
post.comments

user.posts
user.comments

comment.user
comment.post
```

## Release 2: Amazon

Run `createdb amazon`. After you set up your models run `python manage.py makemigrations <appname>` and then `python manage.py migrate`. If you make alterations to your models you may have to rerun these two commands to update your database and get the tests to pass. 

### Models
* Shop
* Product
* Review
* User

### Association Methods
```ruby
shop.owner # should return a User
shop.products # products sold by this shop

product.shop
product.reviews

review.product
review.user

user.reviewed_products
user.shop # if this user owns a shop, returns the shop. For most users this would return nil.
```

## Release 3: Grubhub

Run `createdb grubhub`. After you set up your models run `python manage.py makemigrations` and then `python manage.py migrate`. If you make alterations to your models you may have to rerun these two commands to update your database and get the tests to pass. 

### Models (a.k.a. Tables)
* Users
* Orders 
* Restaurants
* FoodItems 
* OrderFoodItems

### Associations
- A user has many orders
- An order belongs to a user
- A restaurant has many orders
- An order belongs to a restaurant
- An order has many order_food_items
- An order_food_item belongs to an order
- A food item has many order_food_items
- An order_food_item belongs to a food_item
- And finally if you have set up your associations correctly a user should have many food items through orders. See the final test. 
