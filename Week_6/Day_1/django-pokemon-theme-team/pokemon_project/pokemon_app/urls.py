from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pokemon/', views.pick, name='item'),
    path('random/', views.randomize, name='random')
]