"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def rootRouteHandler(request):
    print(request)
    response = HttpResponse("<h1>Welcome to the internet</h1>")
    return response

def anotherHandler(request):
    print("hello world")
    response = HttpResponse("<h2>Get away</h2>")
    response.status_code = 200
    return response

# def picakuRouteHandler(request):
#     print("the world is yours")
#     response = HttpResponse()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rootRouteHandler),
    path('anotherRoute/', anotherHandler)
]
