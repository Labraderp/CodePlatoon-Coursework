"""shapes URL Configuration

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

from django.urls import path
from django.http import HttpResponse
from math import pi

# ========== Goal 1 ========== #

def rect_area_query(request):
    height = request.GET.get('height')
    width = request.GET.get('width')

    area = int(height) * int(width)
    response = HttpResponse(f'<h1>Your rectangle\'s area is {area}')
    return response

def rect_peri_query(request):
    height = request.GET.get('height')
    width = request.GET.get('width')

    perimeter = (int(height) + int(width)) * 2
    response = HttpResponse(f'<h2>Your rectangle\'s perimeter is {perimeter}')
    return response

def circ_area_query(request):
    radius = request.GET.get('radius')

    area = pi * (int(radius) ** 2)
    response = HttpResponse(f"<h1>Your circle's area is {area}")
    return response

def circ_peri_query(request):
    radius = request.GET.get('radius')

    perimeter = pi * (int(radius) * 2)
    response = HttpResponse(f"<h2>Your circle's perimeter is {perimeter}")
    return response

# ========== Goal 2 ========== #

def rect_area(response, height, width):
    area = height * width
    response = HttpResponse(f"<h1>Your rectangle's area is {area}")
    return response

def rect_peri(response, height, width):
    perimeter = (height + width) * 2
    response = HttpResponse(f"<h2>Your rectangle's perimeter is {perimeter}")
    return response

def circ_area(response, radius):
    area = pi * (radius ** 2)
    response = HttpResponse(f"<h1>Your circle's area is {area}")
    return response

def circ_peri(response, radius):
    perimeter = 2 * pi * radius
    response = HttpResponse(f"<h2>Your circle's perimeter is {perimeter}")
    return response

urlpatterns = [
    path('rectangle/area/<int:height>/<int:width>', rect_area),
    path('rectangle/perimeter/<int:height>/<int:width>', rect_peri),
    path('circle/area/<int:radius>', circ_area),
    path('circle/perimeter/<int:radius>', circ_peri),
    path('rectangle/area', rect_area_query),
    path('rectangle/perimeter', rect_peri_query),
    path('circle/area', circ_area_query),
    path('circle/perimeter', circ_peri_query)
]