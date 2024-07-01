# bookings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search-flights/', views.search_flights, name='search_flights'),
     path('search-hotels/', views.search_hotels, name='search_hotels'),
     path('search-packages/', views.search_packages, name='search_packages'),
     path('search-trains/', views.search_trains, name='search_trains'),
     path('search-buses/', views.search_buses, name='search_buses'),
]

